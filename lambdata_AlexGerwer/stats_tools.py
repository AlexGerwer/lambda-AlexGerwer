import numpy as np
import collections as cl

class  Stats:
    """
    General representation of stats for a list
    https://github.com/AlexGerwer/DataScience-ToolBox
    """

    def __init__(self,data):
        """Captures the data"""
        self.data = list(data)
        print ('The data = ', self.data)

    def stat_mean(self):
        """Calculates the mean"""
        self.mean_value=sum(self.data)/len(self.data)
        return self.mean_value

    def stat_median(self):
        self.data.sort()
        if len(self.data) % 2 != 0:
            idx = int((len(self.data) - 1) / 2)
            return self.data[idx]
        else:
            idx_1 = self.data[int((len(self.data) / 2))]
            idx_2 = self.data[int((len(self.data) / 2) - 1)]
            idx = (idx_1 + idx_2) / 2
            return self.data[idx]
        self.median_value=self.data[idx]
        return self.median_value

    def stat_mode(self):
        self_data_list = list(self.data)
        counter = cl.Counter(self_data_list)
        if len(counter) > 1:  # ensure at least 2 unique elements
            possible_mode, next_highest = counter.most_common(2)
            if possible_mode[1] > next_highest[1]:
                self.mode_value = possible_mode[0]
                return self.mode_value
        self.mode_value = np.nan
        return self.mode_value

    def stat_variance(self):
        self_data_array = np.array(self.data)
        self.variance_value = ((self_data_array - self.stat_mean())**2).sum() / (len(self_data_array) - 1)
        return self.variance_value

    def stat_standard_deviation(self):
        self_data_array = np.array(self.data)
        variance_value = ((self_data_array - self.stat_mean())**2).sum() / (len(self_data_array) - 1)
        self.standard_deviation_value = variance_value**(0.5)
        return self.standard_deviation_value

    def stat_coefficient_of_variation(self):
        self.coefficient_of_variation_value = self.stat_standard_deviation() / self.stat_mean()
        return self.coefficient_of_variation_value

    def summary(self):
        return {"Mean": self.stat_mean(), "Median": self.stat_median(),
                "Mode": self.stat_mode(), "Variance": self.stat_variance(),
                "StandardDeviation": self.stat_standard_deviation(),
                "CoefficientOfVariation": self.stat_coefficient_of_variation()}
