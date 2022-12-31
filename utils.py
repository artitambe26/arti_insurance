import numpy as np
import pandas as pd
import pickle
import json
import config

class HealthInsurance():
    def __init__(self,user_data):
        self.user_data = user_data
        self.model_file_path = config.MODEL_FILE_PATH
        self.project_data_path = config.PROJECT_DATA_PATH

    def load_saved_data(self):
        with open(self.model_file_path,"rb") as f:
            self.model = pickle.load(f)
        with open(self.project_data_path,"r") as f:
            self.project_data = json.load(f)

    def health_pred(self):
        self.load_saved_data()
        sex = self.user_data["sex"]
        smoker = self.user_data["smoker"]
        region = self.user_data["region"]

        sex = self.project_data["sex"][sex]
        smoker = self.project_data["smoker"][smoker]

        region = "region_"+region

        region_index = self.project_data["columns"].index(region)

        test_array = np.zeros(len(self.project_data["columns"]))

        test_array[0] = eval(self.user_data["age"])
        test_array[1] = sex
        test_array[2] = eval(self.user_data["bmi"])
        test_array[3] = eval(self.user_data["children"])
        test_array[4] = smoker
        test_array[region_index] = 1

        pred_price = np.around(self.model.predict([test_array])[0],2)
        print("Predicted charges are :",pred_price)
        return pred_price

if __name__ == "__main__":
    obj = HealthInsurance()
    obj 
       
         
        

        

          



