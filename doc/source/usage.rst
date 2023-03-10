Usage
=====

To generate graphs we need to setup a ``GraphGenerator`` object that operates based on a set of settings that correspond to a specific representation. The easiest way to do so is to use one of the implemented settings used in the `publication <https://chemrxiv.org/engage/chemrxiv/article-details/62b8daaf7da6ce76b221a831>`_. In the example below we use the ``baseline`` representation. After the ``GraphGenerator`` is set up we can use it to generate graphs of molecules. For this we need to call the ``.generate_graph()`` function providing it with a dictionary (``qm_data_dict``) of the relevant QM data. The required information and correct formatting of this dictionary is detailed in section :doc:`input`.

.. code-block:: python
   :linenos:

    import HyDGL as HyDGL

    # get the QM data dictionary for the moleulce
    qm_data_dict = # your code for obtaining the dictionary

    # get the default settings for baseline graphs 
    ggs = HyDGL.GraphGeneratorSettings.baseline()
    # setup the graph generator with these settings
    gg = HyDGL.GraphGenerator(settings=ggs)
    # generate a graph according to these settings using a
    # dict of the relevant QM data of a specific molecule
    hydgl_graph = gg.generate_graph(HyDGL.QmData.from_dict(qm_data_dict))


Aside from ``.baseline()`` also the ``.uNatQ()`` and ``.dNatQ()`` representations are implemented. Their exact specifications can be found in the `publication <https://chemrxiv.org/engage/chemrxiv/article-details/62b8daaf7da6ce76b221a831>`_.

The above code will generate the graphs without target values for the use in machine learning applications. To include such targets we can pass a list of target identifiers to the constructor to imbue all generated graphs with these targets. For this we need to make use of the enumeration class ``QmTarget``. In the example below we use two targets, the polarisability and dipole moment.

.. code-block:: python
   :linenos:

    import HyDGL

    # get the QM data dictionary for the moleulce
    qm_data_dict = # your code for obtaining the dictionary

    # set up the list of target identifiers
    target_list = [HyDGL.enums.QmTarget.POLARISABILITY, 
                   HyDGL.enums.QmTarget.TZVP_DIPOLE_MOMENT]

    # get the default settings for baseline graphs 
    ggs = HyDGL.GraphGeneratorSettings.baseline(target_list)
    # setup the graph generator with these settings
    gg = HyDGL.GraphGenerator(settings=ggs)
    # generate a graph according to these settings using a
    # dict of the relevant QM data of a specific molecule
    hydgl_graph = gg.generate_graph(HyDGL.QmData.from_dict(qm_data_dict))

============
Graph export
============

Graph objects can be exported either as ``networkx`` or ``pytorch_geometric`` graphs. 

.. code-block:: python
   :linenos:

    # get networkx object
    nx_graph = hydgl_graph.get_networkx_graph_object()
    # get pytorch object
    pyg_graph = hydgl_graph.get_pytorch_data_object()

Using the respective libraries you can further manipulate the graphs of write them to disc.

This will display the graph in your browser and is done by using the ``plotly`` library. For advanced settings concerning the rendering of plots refer to `their documentation <https://plotly.com/python/>`_.

============
Graph import
============

Graph objects can be imported from ``networkx`` using:

.. code-block:: python
   :linenos:

    hydgl_graph = Graph.from_networkx(nx_graph)

This will display the graph in your browser and is done by using the ``plotly`` library. For advanced settings concerning the rendering of plots refer to `their documentation <https://plotly.com/python/>`_.


===================
Graph visualisation
===================

You can visualise the graph you generated by calling the ``.visualise()`` function of the graph object:

.. code-block:: python
   :linenos:

    graph.visualise()

This will display the graph in your browser and is done by using the ``plotly`` library. For advanced settings concerning the rendering of plots refer to `their documentation <https://plotly.com/python/>`_.

..
    ===============================
    Custom graph generator settings
    ===============================

    You can also specify custom settings for graph generation.