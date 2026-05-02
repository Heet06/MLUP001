#### Problem Statement — Churn Prediction

Customer churn is the process of customers switching from one service provider to another

'Chit-Chat', a telecommunications company is concerned about the number of customers leaving their service

Over a period, they have recorded a lot of data about the customers including — 
- Demographic information
- Account information
- Services that each customer has signed up for

They have also recorded if a customer has churned out or not within the last month


#### The Dataset

##### DemoDetails.csv

| Variable      | Description                              |
| ------------- | ---------------------------------------- |
| CustomerID    | Unique customer ID                       |
| gender        | Gender of the customer                   |
| SeniorCitizen | Whether the customer is a senior citizen |
| Partner       | Whether the customer has a partner       |
| Dependents    | Whether the customer has dependents      |

- Total Size: 251x5

##### AcDetails.txt
| Variable         | Description                                      |
| ---------------- | ------------------------------------------------ |
| CustomerID       | Unique customer ID                               |
| tenure           | Number of months the customer has stayed         |
| Contract         | Type of contract                                 |
| PaperlessBilling | Whether customer has opted for paperless billing |
| PaymentMethod    | Customer's payment method                        |
| MonthlyCharges   | Monthly charges incurred by the customer         |
| TotalCharges     | Total charges incurred by the customer           |

- Total Size: 251x7

##### ServiceDetails.csv
| Variable         | Description                                |
| ---------------- | ------------------------------------------ |
| CustomerID       | Unique customer ID                         |
| PhoneService     | Whether the customer has phone service     |
| MultipleLines    | Whether the customer has multiple lines    |
| InternetService  | Types of internet service                  |
| OnlineSecurity   | Whether the customer has online security   |
| OnlineBackup     | Whether the customer has online backup     |
| DeviceProtection | Whether the customer has device protection |
| TechSupport      | Whether the customer has tech support      |
| StreamingTV      | Whether the customer has streaming TV      |
| StreamingMovies  | Whether the customer has streaming movies  |
| Churn            | Whether the customer has churned           |
- Size: 251x11

#### Initial Takeaways
- The data is split into 3 different files:
	- demoDetails.csv
	- acDetails.txt
	- serviceDetails.csv

- Each record is at the customer level.
- CustomerID is the primary key

