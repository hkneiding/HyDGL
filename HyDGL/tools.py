class Tools:

    @staticmethod
    def get_one_hot_encoded_feature_dict(feature_dict: dict, class_feature_dict: dict) -> dict:

        """Gets the one-hot encoding of a given feature list according to a given dict.

        Returns:
            dict: Dict of features.
        """

        one_hot_encoded_feature_dict = {}

        for key in feature_dict.keys():

            if key in class_feature_dict.keys():
                one_hot_encoded_feature_dict[key] = (Tools.get_one_hot_encoding(len(class_feature_dict[key]), class_feature_dict[key].index(feature_dict[key])))
            else:
                one_hot_encoded_feature_dict[key] = (feature_dict[key])

        return one_hot_encoded_feature_dict

    @staticmethod
    def get_one_hot_encoded_feature_list(feature_dict: dict, class_feature_dict: dict):

        """Gets the one-hot encoding of a given feature list according to a given dict.

        Returns:
            list[float]: The one-hot encoded feature list.
        """

        one_hot_encoded_feature_dict = Tools.get_one_hot_encoded_feature_dict(feature_dict, class_feature_dict)

        return Tools.flatten_list([one_hot_encoded_feature_dict[key] for key in one_hot_encoded_feature_dict.keys()])

    @staticmethod
    def get_one_hot_encoding(n_classes: int, class_number: int):

        """Helper function that the one hot encoding for one specific element by specifying the number of classes and the class of the current element.

        Raises:
            ValueError: If a class number is requested that is higher than the maximum number of classes.

        Returns:
            list[int]: The one hot encoding of one element.
        """

        if class_number >= n_classes:
            raise ValueError('Cannot get one hot encoding for a class number higher than the number of classes.')

        # return empty list if there is only one type
        if n_classes == 1:
            return []

        return [1 if x == class_number else 0 for x in list(range(n_classes))]

    @staticmethod
    def get_class_feature_keys(feature_dict):

        """Takes a feature dict a determines at which keys non-numerical class features are used.

        Returns:
            list[str]: A list with keys which correspond to non-numerical class features.
        """

        class_feature_keys = []

        # get indices of features that are not numeric and need to be one-hot encoded
        for key in feature_dict.keys():
            if not type(feature_dict[key]) == int and not type(feature_dict[key]) == float:
                class_feature_keys.append(key)

        return class_feature_keys

    @staticmethod
    def get_class_feature_indices(feature_list):

        """Takes a feature list a determines at which positions non-numerical class features are used.

        Returns:
            list[int]: A list with indices denoting at which positions non-numerical class features are used.
        """

        class_feature_indices = []

        # get indices of features that are not numeric and need to be one-hot encoded
        for i in range(len(feature_list)):
            if not type(feature_list[i]) == int and not type(feature_list[i]) == float:
                class_feature_indices.append(i)

        return class_feature_indices

    @staticmethod
    def flatten_list(input_list):

        """Flattens a irregular list. Embeds any sublist as individual values in main list.

        Returns:
            list[]: The flattend list.
        """

        flattend_list = []
        for element in input_list:
            if isinstance(element, list):
                flattend_list.extend(Tools.flatten_list(element))
            else:
                flattend_list.append(element)

        return flattend_list

    @staticmethod
    def calculate_euclidean_distance(x: list[float], y: list[float]) -> float:

        """Calculates the euclidean distance between to points given as lists.

        Returns:
            float: The euclidean distance between the points
        """

        # make sure both lists have the same length
        assert len(x) == len(y)

        # get dimension wise squared distances
        squares = [(a - b) ** 2 for a, b in zip(x, y)]

        # return sum of square root
        return sum(squares) ** 0.5

    @staticmethod
    def calculate_distance_matrix(points: list[list[float]]) -> list[list[float]]:

        """Calculates the distance matrix of a list of points.

        Returns:
            list[list[float]]: The distance matrix.
        """

        # setup matrix
        distance_matrix = [[0 for x in range(len(points))] for y in range(len(points))]

        # iterate over the upper triangle
        for i in range(len(distance_matrix) - 1):
            for j in range(i + 1, len(distance_matrix), 1):
                distance = Tools.calculate_euclidean_distance(points[i], points[j])
                distance_matrix[i][j] = distance
                distance_matrix[j][i] = distance

        return distance_matrix

    @staticmethod
    def min_max_scale(value: float, min_value: float, max_value: float) -> float:

        """Min-max scales a value according to given extremum values

        Raises:
            ValueError: If the given value is lower than the minimum value or higher than the maximum value.

        Returns:
            float: The scaled value.
        """

        if type(value) == str:
            return value

        if min_value > value:
            raise ValueError('Minimum value cannot be larger than current value.')
        if max_value < value:
            raise ValueError('Maximum value cannot be lower than current value.')

        return (value - min_value) / (max_value - min_value)
