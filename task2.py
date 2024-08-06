{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "57c89440-85d6-4149-8b79-0eab166fea7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "372ffc18-40b3-43e8-a15e-fc1ca25e7c93",
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
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>bmi</th>\n",
       "      <th>children</th>\n",
       "      <th>smoker</th>\n",
       "      <th>region</th>\n",
       "      <th>charges</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>19</td>\n",
       "      <td>female</td>\n",
       "      <td>27.900</td>\n",
       "      <td>0</td>\n",
       "      <td>yes</td>\n",
       "      <td>southwest</td>\n",
       "      <td>16884.92400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>18</td>\n",
       "      <td>male</td>\n",
       "      <td>33.770</td>\n",
       "      <td>1</td>\n",
       "      <td>no</td>\n",
       "      <td>southeast</td>\n",
       "      <td>1725.55230</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>28</td>\n",
       "      <td>male</td>\n",
       "      <td>33.000</td>\n",
       "      <td>3</td>\n",
       "      <td>no</td>\n",
       "      <td>southeast</td>\n",
       "      <td>4449.46200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>33</td>\n",
       "      <td>male</td>\n",
       "      <td>22.705</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>21984.47061</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>32</td>\n",
       "      <td>male</td>\n",
       "      <td>28.880</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>3866.85520</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1333</th>\n",
       "      <td>50</td>\n",
       "      <td>male</td>\n",
       "      <td>30.970</td>\n",
       "      <td>3</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>10600.54830</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1334</th>\n",
       "      <td>18</td>\n",
       "      <td>female</td>\n",
       "      <td>31.920</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>northeast</td>\n",
       "      <td>2205.98080</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1335</th>\n",
       "      <td>18</td>\n",
       "      <td>female</td>\n",
       "      <td>36.850</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>southeast</td>\n",
       "      <td>1629.83350</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1336</th>\n",
       "      <td>21</td>\n",
       "      <td>female</td>\n",
       "      <td>25.800</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>southwest</td>\n",
       "      <td>2007.94500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1337</th>\n",
       "      <td>61</td>\n",
       "      <td>female</td>\n",
       "      <td>29.070</td>\n",
       "      <td>0</td>\n",
       "      <td>yes</td>\n",
       "      <td>northwest</td>\n",
       "      <td>29141.36030</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1338 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      age     sex     bmi  children smoker     region      charges\n",
       "0      19  female  27.900         0    yes  southwest  16884.92400\n",
       "1      18    male  33.770         1     no  southeast   1725.55230\n",
       "2      28    male  33.000         3     no  southeast   4449.46200\n",
       "3      33    male  22.705         0     no  northwest  21984.47061\n",
       "4      32    male  28.880         0     no  northwest   3866.85520\n",
       "...   ...     ...     ...       ...    ...        ...          ...\n",
       "1333   50    male  30.970         3     no  northwest  10600.54830\n",
       "1334   18  female  31.920         0     no  northeast   2205.98080\n",
       "1335   18  female  36.850         0     no  southeast   1629.83350\n",
       "1336   21  female  25.800         0     no  southwest   2007.94500\n",
       "1337   61  female  29.070         0    yes  northwest  29141.36030\n",
       "\n",
       "[1338 rows x 7 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=pd.read_csv(r\"C:\\Users\\20115\\Downloads\\Telegram Desktop\\insurance-data.csv\")\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ea53cb8b-515f-49a9-9105-db07cf751ed0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "First few rows of the DataFrame:\n",
      "   age     sex     bmi  children smoker     region      charges\n",
      "0   19  female  27.900         0    yes  southwest  16884.92400\n",
      "1   18    male  33.770         1     no  southeast   1725.55230\n",
      "2   28    male  33.000         3     no  southeast   4449.46200\n",
      "3   33    male  22.705         0     no  northwest  21984.47061\n",
      "4   32    male  28.880         0     no  northwest   3866.85520\n"
     ]
    }
   ],
   "source": [
    "print(\"\\nFirst few rows of the DataFrame:\")\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "87441172-9dea-4fd0-ac63-9f9e00bf3ef9",
   "metadata": {},
   "source": [
    "**What is the percentage of female smokers?**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "285a1b64-bf28-41a2-9045-d96845886808",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Percentage of female smokers: 17.37%\n"
     ]
    }
   ],
   "source": [
    "female_smokers = df[(df['sex'] == 'female') & (df['smoker'] == 'yes')]\n",
    "percentage_female_smokers = (len(female_smokers) / len(df[df['sex'] == 'female'])) * 100\n",
    "print(f\"Percentage of female smokers: {percentage_female_smokers:.2f}%\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1fc8dfd3-9617-4e58-be66-a10fe9606f4d",
   "metadata": {},
   "source": [
    "**Which city has the maximum insurance rate?**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "fb2e9582-abba-4876-8f41-a08b69c5e9b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "City with the maximum insurance rate: southeast\n"
     ]
    }
   ],
   "source": [
    "max_insurance_city = df.groupby('region')['charges'].sum().idxmax()\n",
    "print(f\"City with the maximum insurance rate: {max_insurance_city}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0cfc96fb-a534-49cc-ae71-625198eef3fd",
   "metadata": {},
   "source": [
    "**Which gender has the maximum insurance rate?**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "dbef4d26-e643-4a6c-aca9-6a551d3bccf7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Gender with the maximum insurance rate: male\n"
     ]
    }
   ],
   "source": [
    "max_insurance_gender = df.groupby('sex')['charges'].sum().idxmax()\n",
    "print(f\"Gender with the maximum insurance rate: {max_insurance_gender}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b68ca181-413c-4284-ba7e-6f28a957b5fc",
   "metadata": {},
   "source": [
    "**what is the average percentage of female smoker age?**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "c14f7c04-e20a-41ab-98ca-a0b31d771333",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average age of female smokers: 38.61 years\n"
     ]
    }
   ],
   "source": [
    "average_age_female_smokers = female_smokers['age'].mean()\n",
    "print(f\"Average age of female smokers: {average_age_female_smokers:.2f} years\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd305036-e5ff-4418-a516-5027c4c3c9a3",
   "metadata": {},
   "source": [
    "**What is the percentage of males who has children insurance?**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "0acb47bc-a5d4-4a3b-943c-e567f233f33d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Percentage of males who have children insurance: 57.84%\n"
     ]
    }
   ],
   "source": [
    "males_with_children = df[(df['sex'] == 'male') & (df['children'] > 0)]\n",
    "percentage_males = (len(males_with_children) / len(df[df['sex'] == 'male'])) * 100\n",
    "print(f\"Percentage of males who have children insurance: {percentage_males:.2f}%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "717ebf74-b241-46ab-a68a-583af8a027dc",
   "metadata": {},
   "source": [
    "**What are the percentage of the females who hase children insurance?**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "d442fdb4-d69c-46e7-8312-a2fe7a376502",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Percentage of females who have children insurance: 56.34%\n"
     ]
    }
   ],
   "source": [
    "females_with_children = df[(df['sex'] == 'female') & (df['children'] > 0)]\n",
    "percentage_females = (len(females_with_children) / len(df[df['sex'] == 'female'])) * 100\n",
    "print(f\"Percentage of females who have children insurance: {percentage_females:.2f}%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7da31246-867c-4422-8da7-2fed9f942229",
   "metadata": {},
   "source": [
    "**what are the maximum number of children associated with male parent assurance?**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "e8ca0959-838c-4135-9584-be07d7e0358b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Maximum number of children associated with male parent insurance: 5\n"
     ]
    }
   ],
   "source": [
    "max_children_with_male = df[df['sex'] == 'male']['children'].max()\n",
    "print(f\"Maximum number of children associated with male parent insurance: {max_children_with_male}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1cc78e9e-7b14-440b-9475-0b9c6bf12b0e",
   "metadata": {},
   "source": [
    "**what are the maximum number of children associated with female parent assurance?**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "1a64db92-47c2-4957-a994-360ebfe6c73a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Maximum number of children associated with female parent insurance: 5\n"
     ]
    }
   ],
   "source": [
    "max_children_with_female = df[df['sex'] == 'male']['children'].max()\n",
    "print(f\"Maximum number of children associated with female parent insurance: {max_children_with_female}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6341c58a-0e16-4c27-baf2-e0d670015ac1",
   "metadata": {},
   "source": [
    "**Which city has the maximum female insurance total charge?**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "445204a6-2755-48f0-b1dc-10200ae34e7a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "City with the maximum female insurance total charge: southeast\n"
     ]
    }
   ],
   "source": [
    "city_with_the_maximum_female_insurance=df[df['sex']=='female'].groupby('region')['charges'].sum() .idxmax()\n",
    "print(f\"City with the maximum female insurance total charge: {city_with_the_maximum_female_insurance}\")"
   ]
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
