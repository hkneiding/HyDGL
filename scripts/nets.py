import numpy as np
import torch
import torch.nn.functional as F
from torch.nn import GRU, Linear, ReLU, Sequential
from torch_geometric.nn import NNConv, Set2Set


class GilmerNet(torch.nn.Module):

    def __init__(self, n_node_features, n_edge_features, dim=64, set2set_steps=3, n_atom_jumps=3, aggr_function='mean'):
        super().__init__()

        self.n_atom_jumps = n_atom_jumps

        self.lin0 = torch.nn.Linear(n_node_features, dim)

        nn = Sequential(Linear(n_edge_features, 128), ReLU(), Linear(128, dim * dim))
        self.conv = NNConv(dim, dim, nn, aggr=aggr_function)
        self.gru = GRU(dim, dim)

        self.set2set = Set2Set(dim, processing_steps=set2set_steps)
        self.lin1 = torch.nn.Linear(2 * dim, dim)
        self.lin2 = torch.nn.Linear(dim, 1)

    def forward(self, data):
        out = F.relu(self.lin0(data.x))
        h = out.unsqueeze(0)

        for i in range(self.n_atom_jumps):
            m = F.relu(self.conv(out, data.edge_index, data.edge_attr))
            out, h = self.gru(m.unsqueeze(0), h)
            out = out.squeeze(0)

        out = self.set2set(out, data.batch)
        out = F.relu(self.lin1(out))
        out = self.lin2(out)
        return out.view(-1)


class GilmerNetGraphLevelFeatures(torch.nn.Module):

    def __init__(self, n_node_features, n_edge_features, n_graph_features, dim=64, set2set_steps=3, n_atom_jumps=3, aggr_function='mean'):
        super().__init__()

        self.n_atom_jumps = n_atom_jumps

        self.lin0 = torch.nn.Linear(n_node_features, dim)

        nn = Sequential(Linear(n_edge_features, 128), ReLU(), Linear(128, dim * dim))
        self.conv = NNConv(dim, dim, nn, aggr=aggr_function)
        self.gru = GRU(dim, dim)

        self.set2set = Set2Set(dim, processing_steps=set2set_steps)
        self.lin1 = torch.nn.Linear(2 * dim + n_graph_features, dim)
        self.lin2 = torch.nn.Linear(dim, 1)

    def forward(self, data):
        out = F.relu(self.lin0(data.x))
        h = out.unsqueeze(0)

        for i in range(self.n_atom_jumps):
            m = F.relu(self.conv(out, data.edge_index, data.edge_attr))
            out, h = self.gru(m.unsqueeze(0), h)
            out = out.squeeze(0)

        out = self.set2set(out, data.batch)

        # concatenate graph features to embedding vector
        batch_size = len(np.unique(data.batch.detach().numpy()))
        graph_attr = data.graph_attr.reshape((batch_size, -1))
        out = torch.cat((out, graph_attr), dim=1)

        out = F.relu(self.lin1(out))
        out = self.lin2(out)
        return out.view(-1)
