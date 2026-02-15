import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D

#Scaling the dataset
data=pd.read_csv("student_performance.csv")
data=data.drop(columns="grade")
scalar=StandardScaler()
columns_Scaled=["student_id","weekly_self_study_hours","attendance_percentage","class_participation"]
data[columns_Scaled]=scalar.fit_transform(data[columns_Scaled])

print("The null values in the Dataset : ")
print(data.isnull().sum())
print()
print()
print("The scaled data is : ")
print(data)


x=data[["weekly_self_study_hours","attendance_percentage","class_participation"]]
y=data["total_score"]
#training the model
model=LinearRegression()
model.fit(x,y)
#making the prediciton
predicted_scores=model.predict(x)

mae=mean_absolute_error(y,predicted_scores)
mse=mean_squared_error(y,predicted_scores)
rmse=np.sqrt(mse)
r2=r2_score(y,predicted_scores)

print("-"*50)
print("mean_absolute_error : ",mae)
print("mean_squared_error : ",mse)
print("root mean sqquared error : ",rmse)
print("r2 score (Model Accuracy) : ",r2)
print("-"*50)

plt.figure()
plt.hist(data["total_score"],bins=30,color="red",edgecolor="black")
plt.title("Distribution of final exam score")
plt.xlabel("Final Exam Score")
plt.ylabel("Number of Students")
plt.grid(True)


sample_data = data.sample(n=5000, random_state=42)
x_sample=sample_data[["weekly_self_study_hours","attendance_percentage","class_participation"]]
sample_predicted_scores=model.predict(x_sample)

fig = plt.figure(figsize=(10, 20))
ax = fig.add_subplot(111, projection='3d')

# We'll plot two features and the result
# x = Hours, y = Attendance, z = Actual Score
ax.scatter(sample_data['weekly_self_study_hours'], 
           sample_data['attendance_percentage'], 
           sample_data['total_score'], 
            cmap='viridis', alpha=0.05)
ax.plot(sample_data['weekly_self_study_hours'], sample_data['attendance_percentage'],sample_predicted_scores,c="red",label="Predicted score" )
ax.set_xlabel('Study Hours')
ax.set_ylabel('Attendance %')
ax.set_zlabel('Total Score')
plt.title("3D View of Student Performance")
plt.show()

my_input = [[15, 95, 80]]

my_input_scaled = scalar.fit_transform(my_input)


my_prediction = model.predict(my_input_scaled)

print(f"Final  Prediction made by the model : {my_prediction[0]}")