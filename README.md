# ECS 171 Machine Learning Project Group 5

## Introduction

Welcome to our ECS 171 Machine Learning project repository. This project includes an API, a frontend, and various Jupyter notebooks for different machine learning models. Our API is built with Flask and hosted on Google Cloud Run, while the frontend is developed using Next.js and hosted on Vercel.

**Important Note on Backend Cold Starts**

## Project Structure

- **API**: Contains the Flask backend server (`app.py`). Hosted on Google Cloud Run, note .
- **Frontend**: Developed in Next.js. Hosted on Vercel at [ml.lpu.nz](https://ml.lpu.nz).
    - When using our Flask API hosted on Google Cloud Run, it's crucial to allow the backend server time to get past its cold starts before attempting to run the demo. This is specific to the version hosted on Google Cloud Run and is not an issue when running the server locally.
    - The server might initially show "Backend: Disconnected" on the frontend. If this happens, please refresh the page a few times until it displays "Backend: Connected". This indicates that the backend has successfully warmed up and is ready to handle requests efficiently.
- **Jupyter Notebooks**: Located in the root directory, including `ANN.ipynb`, `decision_tree.ipynb`, `EDA.ipynb`, `histogram_and_pair_plot.ipynb`, `logistic.ipynb`, `Naive_Bayes.ipynb`, `random_forest.ipynb`, `SVM.ipynb`.

## Installation and Setup
[Video Tutorial](https://drive.google.com/file/d/11-k7_zFbdooiE9jKfJvr-d6x6G5dE-dK/view)

### Backend

1. Clone the repository.
2. Navigate to the `api` folder.
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the Flask server locally.
    ```
    python app.py
    ```

### Frontend

1. Navigate to the `frontend` folder.
2. Ensure `pnpm` is installed. If not, install it:
   ```
   npm install -g pnpm
   ```
3. Install dependencies:
   ```
   pnpm install
   ```
4. Run the Next.js server locally.
   ```
   pnpm dev
   ```

### Hosting and Deployment

- The frontend is hosted on Vercel and the backend on Google Cloud Run.
- Note: The backend server might need some time to warm up. Check if the frontend displays "Backend: Connected". If it shows "Backend: Disconnected", refresh the page a few times.

## Contributors

- [Lucas Punz](https://github.com/lucaspunz)
- [Amar Singh](https://github.com/am7r)
- [Joe Zhu](https://github.com/AlundorZhu)
- [Zhenshuo Xu](https://github.com/sodqwq)
- [Omar Taha](https://github.com/iu7u13)
