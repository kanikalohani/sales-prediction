{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Simple Linear Regression"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1: Reading and Understanding the Data\n",
    "\n",
    "1. Importing data using the pandas library\n",
    "2. Understanding the structure of the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Supress Warnings\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import the numpy and pandas package\n",
    "\n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>TV</th>\n",
       "      <th>Radio</th>\n",
       "      <th>Newspaper</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>230.1</td>\n",
       "      <td>37.8</td>\n",
       "      <td>69.2</td>\n",
       "      <td>22.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>44.5</td>\n",
       "      <td>39.3</td>\n",
       "      <td>45.1</td>\n",
       "      <td>10.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>17.2</td>\n",
       "      <td>45.9</td>\n",
       "      <td>69.3</td>\n",
       "      <td>12.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>151.5</td>\n",
       "      <td>41.3</td>\n",
       "      <td>58.5</td>\n",
       "      <td>16.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>180.8</td>\n",
       "      <td>10.8</td>\n",
       "      <td>58.4</td>\n",
       "      <td>17.9</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      TV  Radio  Newspaper  Sales\n",
       "0  230.1   37.8       69.2   22.1\n",
       "1   44.5   39.3       45.1   10.4\n",
       "2   17.2   45.9       69.3   12.0\n",
       "3  151.5   41.3       58.5   16.5\n",
       "4  180.8   10.8       58.4   17.9"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Read the given CSV file, and view some sample records\n",
    "\n",
    "advertising = pd.read_csv(\"advertising.csv\")\n",
    "advertising.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##inspecting data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(200, 4)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "advertising.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 200 entries, 0 to 199\n",
      "Data columns (total 4 columns):\n",
      "TV           200 non-null float64\n",
      "Radio        200 non-null float64\n",
      "Newspaper    200 non-null float64\n",
      "Sales        200 non-null float64\n",
      "dtypes: float64(4)\n",
      "memory usage: 6.3 KB\n"
     ]
    }
   ],
   "source": [
    "advertising.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>TV</th>\n",
       "      <th>Radio</th>\n",
       "      <th>Newspaper</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>200.000000</td>\n",
       "      <td>200.000000</td>\n",
       "      <td>200.000000</td>\n",
       "      <td>200.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>147.042500</td>\n",
       "      <td>23.264000</td>\n",
       "      <td>30.554000</td>\n",
       "      <td>15.130500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>85.854236</td>\n",
       "      <td>14.846809</td>\n",
       "      <td>21.778621</td>\n",
       "      <td>5.283892</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.700000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.300000</td>\n",
       "      <td>1.600000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>74.375000</td>\n",
       "      <td>9.975000</td>\n",
       "      <td>12.750000</td>\n",
       "      <td>11.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>149.750000</td>\n",
       "      <td>22.900000</td>\n",
       "      <td>25.750000</td>\n",
       "      <td>16.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>218.825000</td>\n",
       "      <td>36.525000</td>\n",
       "      <td>45.100000</td>\n",
       "      <td>19.050000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>296.400000</td>\n",
       "      <td>49.600000</td>\n",
       "      <td>114.000000</td>\n",
       "      <td>27.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               TV       Radio   Newspaper       Sales\n",
       "count  200.000000  200.000000  200.000000  200.000000\n",
       "mean   147.042500   23.264000   30.554000   15.130500\n",
       "std     85.854236   14.846809   21.778621    5.283892\n",
       "min      0.700000    0.000000    0.300000    1.600000\n",
       "25%     74.375000    9.975000   12.750000   11.000000\n",
       "50%    149.750000   22.900000   25.750000   16.000000\n",
       "75%    218.825000   36.525000   45.100000   19.050000\n",
       "max    296.400000   49.600000  114.000000   27.000000"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "advertising.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2: Visualising the Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt \n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x245652a7fd0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pairplot(advertising, x_vars=['TV', 'Newspaper', 'Radio'], y_vars='Sales',size=4, aspect=1, kind='scatter')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x24568ca9400>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(advertising.corr(), cmap=\"YlGnBu\", annot = True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#The variable 'TV' appears to be most linked with 'Sales', as can be seen from the pairplot and the heatmap. So let's conduct a straightforward linear regression with \"TV\" as the feature variable."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "## Step 3: Performing Simple Linear Regression\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = advertising['TV']\n",
    "y = advertising['Sales']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Train-Test Split\n",
    "\n",
    "70-30 % split."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "74     213.4\n",
       "3      151.5\n",
       "185    205.0\n",
       "26     142.9\n",
       "90     134.3\n",
       "Name: TV, dtype: float64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Let's now take a look at the train dataset\n",
    "\n",
    "X_train.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "74     17.0\n",
       "3      16.5\n",
       "185    22.6\n",
       "26     15.0\n",
       "90     14.0\n",
       "Name: Sales, dtype: float64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Building a Linear Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "import statsmodels.api as sm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add a constant to get an intercept\n",
    "X_train_sm = sm.add_constant(X_train)\n",
    "\n",
    "# Fit the resgression line using 'OLS'\n",
    "lr = sm.OLS(y_train, X_train_sm).fit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "const    6.948683\n",
       "TV       0.054546\n",
       "dtype: float64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Print the parameters, i.e. the intercept and the slope of the regression line fitted\n",
    "lr.params"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                            OLS Regression Results                            \n",
      "==============================================================================\n",
      "Dep. Variable:                  Sales   R-squared:                       0.816\n",
      "Model:                            OLS   Adj. R-squared:                  0.814\n",
      "Method:                 Least Squares   F-statistic:                     611.2\n",
      "Date:                Thu, 13 Sep 2018   Prob (F-statistic):           1.52e-52\n",
      "Time:                        22:39:43   Log-Likelihood:                -321.12\n",
      "No. Observations:                 140   AIC:                             646.2\n",
      "Df Residuals:                     138   BIC:                             652.1\n",
      "Df Model:                           1                                         \n",
      "Covariance Type:            nonrobust                                         \n",
      "==============================================================================\n",
      "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
      "------------------------------------------------------------------------------\n",
      "const          6.9487      0.385     18.068      0.000       6.188       7.709\n",
      "TV             0.0545      0.002     24.722      0.000       0.050       0.059\n",
      "==============================================================================\n",
      "Omnibus:                        0.027   Durbin-Watson:                   2.196\n",
      "Prob(Omnibus):                  0.987   Jarque-Bera (JB):                0.150\n",
      "Skew:                          -0.006   Prob(JB):                        0.928\n",
      "Kurtosis:                       2.840   Cond. No.                         328.\n",
      "==============================================================================\n",
      "\n",
      "Warnings:\n",
      "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n"
     ]
    }
   ],
   "source": [
    "# Performing a summary operation lists out all the different parameters of the regression line fitted\n",
    "print(lr.summary())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The values we are concerned with- \n",
    "1. The coefficients and significance (p-values)\n",
    "2. R-squared\n",
    "3. F statistic and its significance"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The coefficient for TV is 0.054, with a very low p value"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "R - squared is 0.816"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "F statistic has a very low p value (practically low)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x245694aedd8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(X_train, y_train)\n",
    "plt.plot(X_train, 6.948 + 0.054*X_train, 'r')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Residual analysis "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_train_pred = lr.predict(X_train_sm)\n",
    "res = (y_train - y_train_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x245694ba7b8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = plt.figure()\n",
    "sns.distplot(res, bins = 15)\n",
    "fig.suptitle('Error Terms', fontsize = 15)                  # Plot heading \n",
    "plt.xlabel('y_train - y_train_pred', fontsize = 15)         # X-label\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The residuals are following the normally distributed with a mean 0. All good!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Looking for patterns in the residuals"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x245698f7048>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(X_train,res)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5: Predictions on the Test Set\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add a constant to X_test\n",
    "X_test_sm = sm.add_constant(X_test)\n",
    "\n",
    "# Predict the y values corresponding to X_test_sm\n",
    "y_pred = lr.predict(X_test_sm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "126     7.374140\n",
       "104    19.941482\n",
       "99     14.323269\n",
       "92     18.823294\n",
       "111    20.132392\n",
       "dtype: float64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import mean_squared_error\n",
    "from sklearn.metrics import r2_score"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Looking at the RMSE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.019296008966233"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Returns the mean squared error; we'll take a square root\n",
    "np.sqrt(mean_squared_error(y_test, y_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### Checking the R-squared on the test set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7921031601245658"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r_squared = r2_score(y_test, y_pred)\n",
    "r_squared"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Visualizing the fit on the test set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x245698f7e48>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(X_test, y_test)\n",
    "plt.plot(X_test, 6.948 + 0.054 * X_test, 'r')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Linear Regression using linear_model in sklearn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train_lm, X_test_lm, y_train_lm, y_test_lm = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(140,)"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train_lm.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train_lm = X_train_lm.reshape(-1,1)\n",
    "X_test_lm = X_test_lm.reshape(-1,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(140, 1)\n",
      "(140,)\n",
      "(60, 1)\n",
      "(60,)\n"
     ]
    }
   ],
   "source": [
    "print(X_train_lm.shape)\n",
    "print(y_train_lm.shape)\n",
    "print(X_test_lm.shape)\n",
    "print(y_test_lm.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "\n",
    "# Representing LinearRegression as lr(Creating LinearRegression Object)\n",
    "lm = LinearRegression()\n",
    "\n",
    "# Fit the model using lr.fit()\n",
    "lm.fit(X_train_lm, y_train_lm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6.948683200001357\n",
      "[0.05454575]\n"
     ]
    }
   ],
   "source": [
    "print(lm.intercept_)\n",
    "print(lm.coef_)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Same values of Y=mx+c we get now as we got earlier with OLS. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " \n",
    " \n",
    " \n",
    " \n",
    " \n",
    " \n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1.         0.90321277]\n",
      " [0.90321277 1.        ]]\n"
     ]
    }
   ],
   "source": [
    "corrs = np.corrcoef(X_train, y_train)\n",
    "print(corrs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8157933136480384"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corrs[0,1] ** 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "While the true benefits of scaling will be apparent during future modules, at this juncture we can discuss if it has an impact on the model.\n",
    "\n",
    "We'll rebuild the model after scaling the predictor and see what changes.\n",
    "\n",
    "##Standard Scaling\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 100)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### SciKit Learn has these scaling utilities handy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler, MinMaxScaler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "# One aspect that you need to take care of is that the 'fit_transform' can be performed on 2D arrays only. So you need to\n",
    "# reshape your 'X_train_scaled' and 'y_trained_scaled' data in order to perform the standardisation.\n",
    "X_train_scaled = X_train.reshape(-1,1)\n",
    "y_train_scaled = y_train.reshape(-1,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(140, 1)"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train_scaled.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a scaler object using StandardScaler()\n",
    "scaler = StandardScaler()\n",
    "#'Fit' and transform the train set; and transform using the fit on the test set later\n",
    "X_train_scaled = scaler.fit_transform(X_train_scaled)\n",
    "y_train_scaled = scaler.fit_transform(y_train_scaled)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mean and sd for X_train_scaled: 2.5376526277146434e-17 0.9999999999999999\n",
      "mean and sd for y_train_scaled: -2.5376526277146434e-16 1.0\n"
     ]
    }
   ],
   "source": [
    "print(\"mean and sd for X_train_scaled:\", np.mean(X_train_scaled), np.std(X_train_scaled))\n",
    "print(\"mean and sd for y_train_scaled:\", np.mean(y_train_scaled), np.std(y_train_scaled))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Let's fit the regression line following exactly the same steps as done before\n",
    "X_train_scaled = sm.add_constant(X_train_scaled)\n",
    "\n",
    "lr_scaled = sm.OLS(y_train_scaled, X_train_scaled).fit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-2.91433544e-16,  9.03212773e-01])"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Check the parameters\n",
    "lr_scaled.params"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As you might notice, the value of the parameters have changed since we have changed the scale."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's look at the statistics of the model, to see if any other aspect of the model has changed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                            OLS Regression Results                            \n",
      "==============================================================================\n",
      "Dep. Variable:                      y   R-squared:                       0.816\n",
      "Model:                            OLS   Adj. R-squared:                  0.814\n",
      "Method:                 Least Squares   F-statistic:                     611.2\n",
      "Date:                Thu, 13 Sep 2018   Prob (F-statistic):           1.52e-52\n",
      "Time:                        22:39:46   Log-Likelihood:                -80.233\n",
      "No. Observations:                 140   AIC:                             164.5\n",
      "Df Residuals:                     138   BIC:                             170.3\n",
      "Df Model:                           1                                         \n",
      "Covariance Type:            nonrobust                                         \n",
      "==============================================================================\n",
      "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
      "------------------------------------------------------------------------------\n",
      "const      -2.914e-16      0.037  -7.98e-15      1.000      -0.072       0.072\n",
      "x1             0.9032      0.037     24.722      0.000       0.831       0.975\n",
      "==============================================================================\n",
      "Omnibus:                        0.027   Durbin-Watson:                   2.196\n",
      "Prob(Omnibus):                  0.987   Jarque-Bera (JB):                0.150\n",
      "Skew:                          -0.006   Prob(JB):                        0.928\n",
      "Kurtosis:                       2.840   Cond. No.                         1.00\n",
      "==============================================================================\n",
      "\n",
      "Warnings:\n",
      "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n"
     ]
    }
   ],
   "source": [
    "print(lr_scaled.summary())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
