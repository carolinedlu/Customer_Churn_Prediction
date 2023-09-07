# Customer Churn Prediction
Overview
This project aims to predict customer churn in a telecommunications company using machine learning techniques, particularly a neural network model. Customer churn refers to the phenomenon where customers switch from one service provider to another or cancel their subscriptions, which can result in significant revenue loss for businesses.

In this project, we have developed a predictive model that can identify customers who are likely to churn, allowing the company to take proactive measures to retain them. We used a neural network model trained on historical customer data to make these predictions.

![Screenshot (160)](https://github.com/Samarjeet-singh-chhabra/Customer_Churn_Prediction/assets/67777707/6196c88d-160f-4ee5-a725-4b768f9b8811)


# Business context
Customer churn, also known as customer attrition, is a critical concern for businesses across various industries. It refers to the phenomenon where customers discontinue their usage of a product or service offered by a company. In the context of our business, Sunbase, understanding and mitigating customer churn is of utmost importance to ensure the sustainability and growth of our enterprise.


A successful customer churn prediction model can have several positive impacts on our business:

*  **Improved Customer Retention**: By identifying customers at risk of churning, we can implement retention strategies tailored to their needs, thereby reducing the churn rate.

*  **Cost Savings**: Lower churn rates lead to cost savings in terms of customer acquisition and onboarding expenses.

* **Enhanced Customer Satisfaction**: Proactive engagement and personalized offers can enhance the overall customer experience, increasing satisfaction and loyalty.

*  **Revenue Growth**: Retaining customers who might have otherwise churned contributes to revenue growth and long-term profitability.


# Data Understanding

Our Data set has 100000 obervasations and , 9 columns/features.

This dataset contains information about customers and their attributes, as well as their churn status (whether they've discontinued the service or not). Let's briefly explain each column:

*  **CustomerID**: A unique identifier for each customer.

*  **Name**: The name or identifier of the customer.

*  **Age**: The age of the customer.

*  **Gender**: The gender of the customer (Male/Female).

*  **Location**: The location where the customer is based (e.g., Los Angeles, New York, Miami).

*  **Subscription_Length_Months**: The duration of the customer's subscription in months.

*  **Monthly_Bill**: The amount billed to the customer on a monthly basis.

*  **Total_Usage_GB**: The total data usage in gigabytes (GB) by the customer.

*  Churn: This is the target variable, which indicates whether the customer has churned (1) or not (0).

      *  Churn = 1 implies that the customer has discontinued the service.
      *  Churn = 0 implies that the customer is still using the service.
 
  
# Getting Started
Follow these steps to get the project up and running on your local machine.

## 1. Clone the Repository
Clone this repository to your local machine using the following command:

```
git clone https://github.com/Samarjeet-singh-chhabra/Customer_Churn_Prediction.git
```

## 2. Create a Virtual Environment
We recommend using Conda to create a virtual environment for this project. Navigate to the project directory and run the following command to create a Conda environment:

```python
conda create --name churn-env python
```
Activate the virtual environment:

```
conda activate churn-env
```
## 3. Install Requirements
Install the required Python packages by running the following command:

```
pip install -r requirements.txt
```
## 4. Train the Model
To train the predictive model and save all the required files in the "artifacts" folder, execute the training pipeline script by going to the src-->pipelines folder:

```
python train_pipeline.py
```
## 5. Run the Web App
I have developed a Streamlit-based web application for making customer churn predictions. To run the app, go to the parent folder and use the following command:

```
streamlit run app.py
```
Once the Streamlit app is running, you can input customer information, and the app will provide a churn prediction. It will indicate whether the customer is likely to stay (churn: No) or likely to churn (churn: Yes) based on the trained model.

## Contributing
If you would like to contribute to this project, please feel free to work on it.

## License
> This project is licensed under the `MIT License`. See the LICENSE file for details.
