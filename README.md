# ConnectCraft: Simplifying Network Choices

**ConnectCraft** is an AI-powered system designed to address the challenges of selecting the best network service provider for a specific location. By leveraging historical and real-time data, the project aims to accurately predict network performance, empowering users to make informed decisions. This system ensures seamless connectivity and optimal performance, tailored to the geographical needs of its users.

Network selection can be daunting due to varying performance across providers and regions. ConnectCraft solves this problem by integrating advanced machine learning algorithms, real-time data processing, and user feedback mechanisms to predict and recommend the best options for users. The platform emphasizes transparency, informed decision-making, and an enhanced user experience.

The scope of the project is broad, encompassing key areas such as functionality, user experience, security, scalability, and documentation. It includes features like real-time and historical data analysis, user-friendly interfaces for location input, provider recommendations, and feedback integration. The project is designed to grow with future user demands, maintaining ethical compliance and data privacy while optimizing system performance.

The software stack includes robust operating systems like Ubuntu or Windows, programming languages such as Python, JavaScript, and Java/C++, and frameworks like TensorFlow, PyTorch, and Django. For data storage, ConnectCraft utilizes MySQL or MongoDB, while visualization tools such as Matplotlib and Plotly provide intuitive insights. Cloud platforms like AWS, Azure, or GCP are employed for scalability, and NVIDIA GPUs handle AI model training to ensure high-performance computation.

The system is divided into various functional modules. Data is ingested and preprocessed to clean and normalize it for analysis. A storage system manages historical and real-time datasets, while AI/ML models are trained and deployed for accurate predictions. The recommendation engine analyzes user preferences and predicted network performance to suggest suitable providers. A feedback loop continuously collects and evaluates user responses to improve predictions. Additionally, the system monitors health, scales efficiently, and provides analytics for stakeholders.

The design incorporates detailed diagrams such as entity-relationship, sequence, data flow, and class diagrams to illustrate system interactions and architecture. Historical data from multiple locations was converted to usable formats like CSV, enabling performance evaluation for major providers such as VI India, Airtel, and Jio 4G. The results highlight provider performance across diverse geographical areas, empowering users with actionable insights.

ConnectCraft also features a user-friendly interface that allows users to input their location, view network predictions, compare providers, and provide feedback. This intuitive design ensures that users can easily access and understand the information they need to make informed choices.

---

## Data Generation

Android Studio’s robustness and end-to-end support enable dynamic data generation for the speed test application, aimed at collecting comprehensive network performance metrics. The application captures geolocation coordinates, upload and download speeds, ping times, network provider information, and timestamps. These metrics are stored in Firebase and later converted from JSON to CSV format for detailed analysis.

The application is developed using Android Studio, leveraging essential functionalities and libraries to ensure precise data capture. It utilizes the device’s GPS to record geolocation coordinates, measures upload and download speeds, calculates ping times, and identifies the network provider based on device settings and SIM card information. Timestamps are generated using the device’s internal clock when each speed test is conducted.

Data transmission is streamlined through JSON formatting, enabling efficient storage in Firebase, a scalable NoSQL database. Each speed test result is stored as a structured JSON object, facilitating organized and accessible data retrieval. The JSON data is then converted to CSV format using Python-based scripting tools. This conversion simplifies data analysis and modeling, ensuring that the collected metrics are optimized for comprehensive evaluation and strategic insights.

The speed test application’s data generation process is designed to be efficient and effective, ensuring thorough data capture, secure storage, and seamless conversion for insightful analysis and informed decision-making in network performance assessment.

---

## ML Approach

The machine learning model employs several libraries: `pandas` for data manipulation, `numpy` for numerical computing, `scikit-learn` for machine learning algorithms and evaluation metrics, and `mlxtend` for advanced functionalities like `StackingRegressor`. Preprocessing involves removing null values and duplicates to ensure data integrity and reduce noise, thereby improving model performance.

The computation logic uses the `cdist` function from `scipy` to calculate pairwise distances between input coordinates and dataset coordinates. A threshold distance set to 70% of the maximum calculated distance determines similarity. Relevant rows within this threshold are identified for further analysis.

The dataset is split into training and testing sets to prevent overfitting and ensure generalization. Features are standardized using `StandardScaler` to remove the mean and scale to unit variance, ensuring equal contribution from each feature and improving model performance.

A stacking ensemble model is used, combining multiple base regression models (e.g., `RandomForestRegressor`, `GradientBoostingRegressor`, `SVR`) with a meta-regressor (`Ridge`). The base models independently learn patterns, while the meta-regressor optimally combines their predictions to enhance accuracy. This approach effectively handles multicollinearity and leverages the strengths of each base model.

The prediction logic iterates over network providers, calculating the mean predicted bandwidth using the stacking model and selecting the best provider based on predictions. Relevant features are selected, scaled, and used to determine the optimal network provider, ensuring robust and accurate bandwidth predictions.

---

