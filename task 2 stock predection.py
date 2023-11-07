{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "91f4a1b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('STOCK PREDECTION.CSV')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "4014ce41",
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "import warnings\n",
    "warnings.simplefilter(\"ignore\")\n",
    "\n",
    "pd.set_option(\"display.max_columns\",None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d2db2101",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 15000 entries, 0 to 14999\n",
      "Data columns (total 22 columns):\n",
      " #   Column                    Non-Null Count  Dtype  \n",
      "---  ------                    --------------  -----  \n",
      " 0   Patient ID                15000 non-null  int64  \n",
      " 1   Patient Name              15000 non-null  object \n",
      " 2   Age                       15000 non-null  int64  \n",
      " 3   Gender                    15000 non-null  object \n",
      " 4   Hypertension              15000 non-null  int64  \n",
      " 5   Heart Disease             15000 non-null  int64  \n",
      " 6   Marital Status            15000 non-null  object \n",
      " 7   Work Type                 15000 non-null  object \n",
      " 8   Residence Type            15000 non-null  object \n",
      " 9   Average Glucose Level     15000 non-null  float64\n",
      " 10  Body Mass Index (BMI)     15000 non-null  float64\n",
      " 11  Smoking Status            15000 non-null  object \n",
      " 12  Alcohol Intake            15000 non-null  object \n",
      " 13  Physical Activity         15000 non-null  object \n",
      " 14  Stroke History            15000 non-null  int64  \n",
      " 15  Family History of Stroke  15000 non-null  object \n",
      " 16  Dietary Habits            15000 non-null  object \n",
      " 17  Stress Levels             15000 non-null  float64\n",
      " 18  Blood Pressure Levels     15000 non-null  object \n",
      " 19  Cholesterol Levels        15000 non-null  object \n",
      " 20  Symptoms                  12500 non-null  object \n",
      " 21  Diagnosis                 15000 non-null  object \n",
      "dtypes: float64(3), int64(5), object(14)\n",
      "memory usage: 2.5+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "7b2841ed",
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
       "      <th>count</th>\n",
       "      <th>unique</th>\n",
       "      <th>top</th>\n",
       "      <th>freq</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Patient Name</th>\n",
       "      <td>15000</td>\n",
       "      <td>13818</td>\n",
       "      <td>Ela Sarna</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Gender</th>\n",
       "      <td>15000</td>\n",
       "      <td>2</td>\n",
       "      <td>Male</td>\n",
       "      <td>7622</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Marital Status</th>\n",
       "      <td>15000</td>\n",
       "      <td>3</td>\n",
       "      <td>Single</td>\n",
       "      <td>5156</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Work Type</th>\n",
       "      <td>15000</td>\n",
       "      <td>4</td>\n",
       "      <td>Private</td>\n",
       "      <td>3863</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Residence Type</th>\n",
       "      <td>15000</td>\n",
       "      <td>2</td>\n",
       "      <td>Rural</td>\n",
       "      <td>7529</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Smoking Status</th>\n",
       "      <td>15000</td>\n",
       "      <td>3</td>\n",
       "      <td>Currently Smokes</td>\n",
       "      <td>5011</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Alcohol Intake</th>\n",
       "      <td>15000</td>\n",
       "      <td>4</td>\n",
       "      <td>Rarely</td>\n",
       "      <td>3821</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Physical Activity</th>\n",
       "      <td>15000</td>\n",
       "      <td>3</td>\n",
       "      <td>High</td>\n",
       "      <td>5060</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Family History of Stroke</th>\n",
       "      <td>15000</td>\n",
       "      <td>2</td>\n",
       "      <td>Yes</td>\n",
       "      <td>7592</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Dietary Habits</th>\n",
       "      <td>15000</td>\n",
       "      <td>7</td>\n",
       "      <td>Paleo</td>\n",
       "      <td>2192</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Blood Pressure Levels</th>\n",
       "      <td>15000</td>\n",
       "      <td>4458</td>\n",
       "      <td>96/70</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Cholesterol Levels</th>\n",
       "      <td>15000</td>\n",
       "      <td>5952</td>\n",
       "      <td>HDL: 50, LDL: 185</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Symptoms</th>\n",
       "      <td>12500</td>\n",
       "      <td>5786</td>\n",
       "      <td>Difficulty Speaking</td>\n",
       "      <td>268</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Diagnosis</th>\n",
       "      <td>15000</td>\n",
       "      <td>2</td>\n",
       "      <td>No Stroke</td>\n",
       "      <td>7532</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                          count unique                  top  freq\n",
       "Patient Name              15000  13818            Ela Sarna     4\n",
       "Gender                    15000      2                 Male  7622\n",
       "Marital Status            15000      3               Single  5156\n",
       "Work Type                 15000      4              Private  3863\n",
       "Residence Type            15000      2                Rural  7529\n",
       "Smoking Status            15000      3     Currently Smokes  5011\n",
       "Alcohol Intake            15000      4               Rarely  3821\n",
       "Physical Activity         15000      3                 High  5060\n",
       "Family History of Stroke  15000      2                  Yes  7592\n",
       "Dietary Habits            15000      7                Paleo  2192\n",
       "Blood Pressure Levels     15000   4458                96/70    14\n",
       "Cholesterol Levels        15000   5952    HDL: 50, LDL: 185     9\n",
       "Symptoms                  12500   5786  Difficulty Speaking   268\n",
       "Diagnosis                 15000      2            No Stroke  7532"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe(include='O').T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "89e2ca57",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style type=\"text/css\">\n",
       "#T_f5598_row0_col0, #T_f5598_row1_col0, #T_f5598_row1_col1, #T_f5598_row1_col2, #T_f5598_row1_col4, #T_f5598_row1_col5, #T_f5598_row1_col6, #T_f5598_row1_col7, #T_f5598_row2_col0, #T_f5598_row2_col1, #T_f5598_row2_col2, #T_f5598_row2_col3, #T_f5598_row2_col4, #T_f5598_row2_col5, #T_f5598_row2_col6, #T_f5598_row2_col7, #T_f5598_row3_col0, #T_f5598_row3_col1, #T_f5598_row3_col2, #T_f5598_row3_col3, #T_f5598_row3_col4, #T_f5598_row3_col5, #T_f5598_row3_col6, #T_f5598_row3_col7, #T_f5598_row4_col0, #T_f5598_row4_col1, #T_f5598_row4_col2, #T_f5598_row4_col4, #T_f5598_row4_col5, #T_f5598_row4_col6, #T_f5598_row4_col7, #T_f5598_row5_col0, #T_f5598_row5_col1, #T_f5598_row5_col2, #T_f5598_row5_col4, #T_f5598_row5_col5, #T_f5598_row5_col6, #T_f5598_row5_col7, #T_f5598_row6_col0, #T_f5598_row6_col1, #T_f5598_row6_col2, #T_f5598_row6_col3, #T_f5598_row6_col4, #T_f5598_row6_col5, #T_f5598_row6_col6, #T_f5598_row6_col7, #T_f5598_row7_col0, #T_f5598_row7_col1, #T_f5598_row7_col2, #T_f5598_row7_col3, #T_f5598_row7_col4, #T_f5598_row7_col5, #T_f5598_row7_col6, #T_f5598_row7_col7 {\n",
       "  background-color: #bde7db;\n",
       "  color: #000000;\n",
       "}\n",
       "#T_f5598_row0_col1, #T_f5598_row0_col2, #T_f5598_row0_col4, #T_f5598_row0_col5, #T_f5598_row0_col6, #T_f5598_row0_col7, #T_f5598_row4_col3 {\n",
       "  background-color: #ffd4ac;\n",
       "  color: #000000;\n",
       "}\n",
       "#T_f5598_row0_col3 {\n",
       "  background-color: #b2dfd8;\n",
       "  color: #000000;\n",
       "}\n",
       "#T_f5598_row1_col3 {\n",
       "  background-color: #4a4fa5;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "#T_f5598_row5_col3 {\n",
       "  background-color: #4167c7;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "</style>\n",
       "<table id=\"T_f5598\">\n",
       "  <thead>\n",
       "    <tr>\n",
       "      <th class=\"blank level0\" >&nbsp;</th>\n",
       "      <th id=\"T_f5598_level0_col0\" class=\"col_heading level0 col0\" >count</th>\n",
       "      <th id=\"T_f5598_level0_col1\" class=\"col_heading level0 col1\" >mean</th>\n",
       "      <th id=\"T_f5598_level0_col2\" class=\"col_heading level0 col2\" >std</th>\n",
       "      <th id=\"T_f5598_level0_col3\" class=\"col_heading level0 col3\" >min</th>\n",
       "      <th id=\"T_f5598_level0_col4\" class=\"col_heading level0 col4\" >25%</th>\n",
       "      <th id=\"T_f5598_level0_col5\" class=\"col_heading level0 col5\" >50%</th>\n",
       "      <th id=\"T_f5598_level0_col6\" class=\"col_heading level0 col6\" >75%</th>\n",
       "      <th id=\"T_f5598_level0_col7\" class=\"col_heading level0 col7\" >max</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th id=\"T_f5598_level0_row0\" class=\"row_heading level0 row0\" >Patient ID</th>\n",
       "      <td id=\"T_f5598_row0_col0\" class=\"data row0 col0\" >15000.000000</td>\n",
       "      <td id=\"T_f5598_row0_col1\" class=\"data row0 col1\" >49716.000000</td>\n",
       "      <td id=\"T_f5598_row0_col2\" class=\"data row0 col2\" >29001.000000</td>\n",
       "      <td id=\"T_f5598_row0_col3\" class=\"data row0 col3\" >1.000000</td>\n",
       "      <td id=\"T_f5598_row0_col4\" class=\"data row0 col4\" >24562.000000</td>\n",
       "      <td id=\"T_f5598_row0_col5\" class=\"data row0 col5\" >49448.000000</td>\n",
       "      <td id=\"T_f5598_row0_col6\" class=\"data row0 col6\" >75112.000000</td>\n",
       "      <td id=\"T_f5598_row0_col7\" class=\"data row0 col7\" >99975.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th id=\"T_f5598_level0_row1\" class=\"row_heading level0 row1\" >Age</th>\n",
       "      <td id=\"T_f5598_row1_col0\" class=\"data row1 col0\" >15000.000000</td>\n",
       "      <td id=\"T_f5598_row1_col1\" class=\"data row1 col1\" >54.000000</td>\n",
       "      <td id=\"T_f5598_row1_col2\" class=\"data row1 col2\" >21.000000</td>\n",
       "      <td id=\"T_f5598_row1_col3\" class=\"data row1 col3\" >18.000000</td>\n",
       "      <td id=\"T_f5598_row1_col4\" class=\"data row1 col4\" >36.000000</td>\n",
       "      <td id=\"T_f5598_row1_col5\" class=\"data row1 col5\" >54.000000</td>\n",
       "      <td id=\"T_f5598_row1_col6\" class=\"data row1 col6\" >72.000000</td>\n",
       "      <td id=\"T_f5598_row1_col7\" class=\"data row1 col7\" >90.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th id=\"T_f5598_level0_row2\" class=\"row_heading level0 row2\" >Hypertension</th>\n",
       "      <td id=\"T_f5598_row2_col0\" class=\"data row2 col0\" >15000.000000</td>\n",
       "      <td id=\"T_f5598_row2_col1\" class=\"data row2 col1\" >0.000000</td>\n",
       "      <td id=\"T_f5598_row2_col2\" class=\"data row2 col2\" >0.000000</td>\n",
       "      <td id=\"T_f5598_row2_col3\" class=\"data row2 col3\" >0.000000</td>\n",
       "      <td id=\"T_f5598_row2_col4\" class=\"data row2 col4\" >0.000000</td>\n",
       "      <td id=\"T_f5598_row2_col5\" class=\"data row2 col5\" >0.000000</td>\n",
       "      <td id=\"T_f5598_row2_col6\" class=\"data row2 col6\" >0.000000</td>\n",
       "      <td id=\"T_f5598_row2_col7\" class=\"data row2 col7\" >1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th id=\"T_f5598_level0_row3\" class=\"row_heading level0 row3\" >Heart Disease</th>\n",
       "      <td id=\"T_f5598_row3_col0\" class=\"data row3 col0\" >15000.000000</td>\n",
       "      <td id=\"T_f5598_row3_col1\" class=\"data row3 col1\" >1.000000</td>\n",
       "      <td id=\"T_f5598_row3_col2\" class=\"data row3 col2\" >1.000000</td>\n",
       "      <td id=\"T_f5598_row3_col3\" class=\"data row3 col3\" >0.000000</td>\n",
       "      <td id=\"T_f5598_row3_col4\" class=\"data row3 col4\" >0.000000</td>\n",
       "      <td id=\"T_f5598_row3_col5\" class=\"data row3 col5\" >1.000000</td>\n",
       "      <td id=\"T_f5598_row3_col6\" class=\"data row3 col6\" >1.000000</td>\n",
       "      <td id=\"T_f5598_row3_col7\" class=\"data row3 col7\" >1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th id=\"T_f5598_level0_row4\" class=\"row_heading level0 row4\" >Average Glucose Level</th>\n",
       "      <td id=\"T_f5598_row4_col0\" class=\"data row4 col0\" >15000.000000</td>\n",
       "      <td id=\"T_f5598_row4_col1\" class=\"data row4 col1\" >129.000000</td>\n",
       "      <td id=\"T_f5598_row4_col2\" class=\"data row4 col2\" >40.000000</td>\n",
       "      <td id=\"T_f5598_row4_col3\" class=\"data row4 col3\" >60.000000</td>\n",
       "      <td id=\"T_f5598_row4_col4\" class=\"data row4 col4\" >95.000000</td>\n",
       "      <td id=\"T_f5598_row4_col5\" class=\"data row4 col5\" >129.000000</td>\n",
       "      <td id=\"T_f5598_row4_col6\" class=\"data row4 col6\" >165.000000</td>\n",
       "      <td id=\"T_f5598_row4_col7\" class=\"data row4 col7\" >200.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th id=\"T_f5598_level0_row5\" class=\"row_heading level0 row5\" >Body Mass Index (BMI)</th>\n",
       "      <td id=\"T_f5598_row5_col0\" class=\"data row5 col0\" >15000.000000</td>\n",
       "      <td id=\"T_f5598_row5_col1\" class=\"data row5 col1\" >27.000000</td>\n",
       "      <td id=\"T_f5598_row5_col2\" class=\"data row5 col2\" >7.000000</td>\n",
       "      <td id=\"T_f5598_row5_col3\" class=\"data row5 col3\" >15.000000</td>\n",
       "      <td id=\"T_f5598_row5_col4\" class=\"data row5 col4\" >21.000000</td>\n",
       "      <td id=\"T_f5598_row5_col5\" class=\"data row5 col5\" >27.000000</td>\n",
       "      <td id=\"T_f5598_row5_col6\" class=\"data row5 col6\" >34.000000</td>\n",
       "      <td id=\"T_f5598_row5_col7\" class=\"data row5 col7\" >40.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th id=\"T_f5598_level0_row6\" class=\"row_heading level0 row6\" >Stroke History</th>\n",
       "      <td id=\"T_f5598_row6_col0\" class=\"data row6 col0\" >15000.000000</td>\n",
       "      <td id=\"T_f5598_row6_col1\" class=\"data row6 col1\" >1.000000</td>\n",
       "      <td id=\"T_f5598_row6_col2\" class=\"data row6 col2\" >1.000000</td>\n",
       "      <td id=\"T_f5598_row6_col3\" class=\"data row6 col3\" >0.000000</td>\n",
       "      <td id=\"T_f5598_row6_col4\" class=\"data row6 col4\" >0.000000</td>\n",
       "      <td id=\"T_f5598_row6_col5\" class=\"data row6 col5\" >1.000000</td>\n",
       "      <td id=\"T_f5598_row6_col6\" class=\"data row6 col6\" >1.000000</td>\n",
       "      <td id=\"T_f5598_row6_col7\" class=\"data row6 col7\" >1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th id=\"T_f5598_level0_row7\" class=\"row_heading level0 row7\" >Stress Levels</th>\n",
       "      <td id=\"T_f5598_row7_col0\" class=\"data row7 col0\" >15000.000000</td>\n",
       "      <td id=\"T_f5598_row7_col1\" class=\"data row7 col1\" >5.000000</td>\n",
       "      <td id=\"T_f5598_row7_col2\" class=\"data row7 col2\" >3.000000</td>\n",
       "      <td id=\"T_f5598_row7_col3\" class=\"data row7 col3\" >0.000000</td>\n",
       "      <td id=\"T_f5598_row7_col4\" class=\"data row7 col4\" >3.000000</td>\n",
       "      <td id=\"T_f5598_row7_col5\" class=\"data row7 col5\" >5.000000</td>\n",
       "      <td id=\"T_f5598_row7_col6\" class=\"data row7 col6\" >8.000000</td>\n",
       "      <td id=\"T_f5598_row7_col7\" class=\"data row7 col7\" >10.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n"
      ],
      "text/plain": [
       "<pandas.io.formats.style.Styler at 0x29b18021450>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe().round().T.style.background_gradient(cmap='icefire')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "c4862eb8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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HDhwQH799VfrNTw8PKRo0aJy/vx5SUlJyeatMiNPnjzWe3PjybaEhAR5++23pUqVKhIWFibTpk2TY8eOiYjIE088IW5ubhIQEGBdnysiUrt2bXn//ffljz/+kFdeeUWOHz8uNWrUYHbB23D972Z6erq888470rBhQ9m9e7ccO3ZMwsPDZcKECSKSsf8dP35cfvzxRylevLi89dZbcuTIEVmyZImMGzdONm7cKGlpaTJz5sz/rVL/02BD5HjXrl3TDh06aNu2bfXTTz/V6tWr69y5cx3GodrHs65fv16Dg4N1/Pjxqqp6/Phxffzxx7VLly4O6zx8+LBWr15dW7RooYmJiXduY+6gPXv26OOPP65lypTRXr166Z9//mk99sMPPziM91VVnTt3rtpsNmtZ27ZttUWLFnrixAmH9c6dO1cnTZqkqv/7WGBkn1u1TXx8vLZv317btWunR44c0ZUrV2qrVq3Uz8/PKvPII49o165d9e+//7aWTZ06VRs0aKDff//9P75GbpfV9TaxsbE6duxY9fPzUx8fH61ataq2bdtWT506paqqkydPVi8vL+3evbv26NFDIyIitHPnzvrbb7+pqmq1atW0devW+t1332lSUpL++eefOmjQIO3UqZPu37//Tm4ebuLatWsO1/7YrwVavHixjhkzxiqjqhoVFaUeHh7WvlKpUiXNly+f+vn56fPPP69RUVGZ9qO5c+eql5cX1+HdxOXLl3X69Onau3dvXbZsWaZrGP38/HTgwIFavXp1jY2NVVXVt99+W3v27Kl79+5VNzc3Xbt2rfWcGjVq6AsvvKCq//eZfv/997VChQqqevd/B6ampurUqVO1Xbt2Dsvt9R44cKBWqlRJP/roIx0+fLiWL19eW7VqpaoZ1+U+8sgj2r59+yyf+9VXX2mTJk3UZrPpiBEjVFVveZ13bnLjfmH/+4cfftB169apququXbu0fPnyDtfeTp8+XV1dXXXr1q2qqlqvXj3t3r17lq9x+PBhrVu3rn7yySf/U13pycpFrp8qVCQj6ScmJsqZM2fk66+/llGjRsnjjz8uoaGhDmcE7GeuAgMDpVSpUrJ161ZJTk4Wf39/qV69uvz5559y9OhRERHZsmWLvPnmm1K6dGmZNWuW5M+f/85uZDazv39nzpyRpKQk+eqrr+Tq1asyePBgq0xMTIyULVtWypcvby0LDQ2VypUry4cffigiIj179pTLly9L+/btZdWqVbJ582bp16+fTJ8+Xdzc3LjP2F3o+uusrm+btWvXSnBwsMTHx4uIyLFjx2Tp0qUyYsQIKVeunDz22GMye/ZsuXr1qsyYMUNERBo3biyHDh1yuGaxZcuWYrPZ5Lvvvsv0Gshgf/+zOpv+yy+/yPr16+Xdd9+Vv/76SxYtWiTnzp2TiRMnSnp6ugwePFj69esnqir+/v7i4uIi+/fvl759+8qFCxdk/vz5kp6eLs8//7w0atRIKlWqJNHR0dK9e3epVKnSnd5UZME+DDctLU3++usv655mf//9t7z++uuycuVKq+zZs2elbNmysmfPHhERadasmXh7e8uaNWtk5syZEhQUJHny5JH9+/fL9OnTRSTj7HZsbKz88ccfTtm+u8n1QzBXr14tjRs3Fk9PT/n000/l8uXLMnDgQHn++eetMm3atJGzZ89KeHi4eHp6yvDhw+XKlSty5MgRKV68uFSpUkUCAwMdZg/s2rWrfPPNNxIbG2t9psuWLSvFixeXq1evOv07ULMYTaL//zYA+v9H7ri4uMipU6dk8uTJ0rRpU+nQoYOkpKTI7t275eOPP5axY8dKjx49ZOzYsbJ06VL5/vvv5dtvvxUfHx+pW7eunDx50pp5MT093drmtm3bytChQ6VQoULWJRnX99jmZjfuFzabTa5evSqtW7eWkydPiojI999/L40bN5Z69erJF198ISEhITJixAipVauW1a49evSQFStWyPnz5yU9PV3mzJkjc+fOleeff976vnjiiSf+t8r+TxENOcKNZz+OHz9u9bwcOnRIX3nlFa1Ro4a+9tprN12H/UzBlClTNDAwUCMjI1VVdc2aNRoUFKRNmjTR6tWra/78+bVz587W7EB3+5mo/+rUqVNarFgxjYuL0xMnTmiJEiV07Nixqqr6+eefa7169RxmCkxJSdFevXrp/fffr6oZ78vu3bu1ZcuWGhQUpEWLFtVHHnnEOguDu9eFCxd0/vz5unHjRlVV3bdvn9psNv3hhx9UNeMMZMWKFa2Zs+yfvx49emj9+vVVVXX37t1at25dq1fY7tlnn9WRI0dqUlLSndqcHGnx4sU6depU6z1Wzfhes5+hvHjxon7yySdavHhxrVatmkZFRTk83/7+rl27Vj08PPTw4cOqqnr16lXdunWrLliwQGNiYu7Q1uB27dy5Ux9//HEtUaKE1q1bV/v3768nT55UVdVevXrpww8/bM14O2/ePK1WrZoeP35cVVWjo6PV399fe/XqpQcOHNDLly/rDz/8oJ06ddLBgwdbvcq5vd137dqlvXr10t27d6uq6pYtW7RAgQLasGFDq1f46tWrOn/+fM2fP7+ePXvWem6FChX0rbfe0r1792poaKgOHDhQX3nlFe3cubOqqs6ePVsLFSqkly5dUtWM31GbzaaLFy+21vHSSy9pz54979Tm3lRcXJympqZaf6elpWXZkzRs2DC12WxaqFAhfeGFF6ye8Q0bNmjBggU1ISFBVf/vd6BJkybasWNHVVWNjIzUBg0a6OTJk63XuFGTJk101KhRWT6WG1w/c7X9ePL8+fP66aefWiOl7O/tAw88oB988IGqZrSLq6urent7a9myZfWVV17J1EN9/vx5LVy4sC5cuFBVVefMmaMtW7bUJ598UletWmWk/oSsXCI5OVkPHz6sVapUUU9PT61Vq5ZOnz7derx3794aGhqq58+fV9XM4ci+k+/YsUNbtGihr776qqpmHMy0adNGg4KCdPr06blmmtH169drs2bNdNu2baqa8YX62GOP6cSJE/X8+fPaoEEDHTJkiFU+JSVFW7RooTabTX/++WeHdf3555+akpJyR+uPm7t+ytfr7dixQ1u2bKn58+e39nf7wUJQUJB27dpVVVW///57rV+/vjXMwP5Zmjlzpvr7+1vrfuKJJ7Rp06Z67Ngx6zVyy+fnVtLT0zU1NTXLEzRLlixRf39/LVeunLZp00bz5cunH3/8sV65ckVVM4bv2IcMBgYGar9+/bRWrVrWULKUlBT9/fffNS4uTnfu3KkdOnTQrl278vm7C5w/f15//PFHVc365Nzly5f1iSeesIZ4rl69Wps3b66tW7dWVdXTp09r7969tXTp0hoXF6e//vqrurm5OQxZX7FihZYrV07r1aun5cqV00KFCmnv3r31yJEjDq97r54cvBX7Nq9du1bLli3rsLxVq1b6wgsvaHx8vLV8xowZGhISohcvXrSWvfnmm1qmTBlNTk7WvXv3apUqVbRQoUI6dOhQTU9P19OnT6uXl5fOnz/fek7r1q31gw8+sL4XP//8c50wYUJ2b24m13/nL1y4UAMDA3XLli2Zyl24cEGnTp2qI0aM0KtXr+pnn32mrVq10tDQUIcQ9u2332rNmjV12bJlqvp/3+2TJ09Wf39/VVW9dOmSduzYUVu1apXpO8i+rlq1aunw4cMz1TG3uf7WCkuXLlVvb2996aWXrGVHjx7VZs2a6cSJE1VVdfv27Wqz2fT99993eN+SkpL0u+++sz7zDRo00GbNmqmqamJiovHPPiHrHmE/MLlRWlqaLliwQEuUKKFvvfWWTpo0SY8cOaI9e/bUEiVKWGd4Z8+erfXq1dOlS5eq6s3H/qalpenTTz+tQUFB1pfrvXrd1a1ERkZqnTp1VDXjWpBRo0apu7u7uri4aFRUlI4YMULLlCmjU6ZM0TNnzuiXX36pPXr00Fq1alln9W58j2+83gB3zu0cXHXr1k3btWunJ0+e1OTkZL1w4YL12MyZM9XLy0vj4uI0Pj5ew8LCtE2bNg7PDwkJ0Y4dO+rly5dVNeNgYsaMGdaZTru0tLR7/iAvPT1dExMT9ZNPPrHuvZeenp5pu6+/Zu3SpUvarFkzq8dYVfWDDz7QatWqWYF27dq1+sADD+hXX31l/bA++OCD+uijj+qVK1f0yJEj2qdPH61cubIWLFhQ27VrZ70+nCctLU2fffZZrVOnjkObX2/ixIn60EMPWX8fPXpUn3jiCXVxcbFOdqWkpGilSpW0R48eOmvWLA0ODtZff/3VYT0XLlzQH374Qb/99tts256cbNWqVdqiRQvrhKuq6ltvvaVNmjTRXbt26alTp3TgwIFaoEABDQsL0y+++MIqd+TIEXVxcdHvvvtOVVVXr16tLVu2dLgOq0WLFtq4ceObvv6pU6es67mc5eTJk5lOOMfGxmq3bt00f/78GhwcrD179rR6wD/77DOH4ydV1QMHDmS6Zj09PV2ff/55bdSokfU78NZbb+mzzz5r9che/5qTJk3SgIAAXbNmTfZu8F3siy++0MaNG2vDhg315Zdftj7Pixcv1pIlS+r777+vqhnHTyVLlrRCrapqlSpVtGPHjrpz505VzQhqH374oXbu3Fk3b96sqhn77PX7ummErBzm77//1okTJ+qmTZtuWmb//v3WGXZV1ZUrV6qfn5/WrVtXz507p6qqZ86c0aZNm+qTTz6pqhlDnkJCQrR///43Xa/9oGXbtm3WcMN7/WDwZg4ePKg2m02rVq2qrq6uWq1aNf3ss880PDxcW7ZsqUuWLNF3331Xy5Urp4ULF9YSJUrookWLdOTIkVq7dm1nVx+3cODAAX3ppZd02rRpevDgQVVV/e2337R69erWF3pMTIzDvn/u3DnNly+fLlq0SFUzzrSVKVNGQ0JC9JtvvtExY8ZoQECAfvPNN3d+g+5Su3bt0pCQEOs9touPj9e3335bH3roIW3RooXu2LFDVTMOZBo0aKCqGd9xw4cP1xIlSmi5cuWs4UYjRozQwMBAKwBv3bpVy5QpoyVLltSvvvpKVTMOIpcvX57lSSncefbflY8++sjhBvfXn31OT0/XUaNGadu2bXX69On6wAMP6H333adt2rTRb775RlNSUqz2XL16tbZu3VoLFy6sjRs3zjS50I2uH46Um9m/zyZOnKihoaEaGxtrLdu1a5dWrVpVvb299b777tNHH31U33//fY2IiFCbzaYjR47UuLg4Vc3oGQgPD7/p6xw7dsyhR0z1zk7okNUxS1pamn7++eeZJrDYu3evVde5c+dqYGCgFeivXLlirevgwYMaEhJiTeJh9/7772uhQoV0ypQpevz4cd2yZYtWqlTJYTKFm938Oi0tTUuXLq3jx4+/Z3vaT506ZZ1kzKpd5s2bp5UqVdJXX31VFy5cqE899ZSWK1fOej9ee+01LVOmjHWZRaVKlXTatGnW83/66Sdt0qSJlihRQp966in18fHR0qVL63vvvWeNfshuhKy7WFZndnft2qUvvPCCHjp0yKFcQkKCjhs3TkuUKKGlS5fWoKAga5zvuXPntEmTJvrII49Yz7l27ZpOnz5d8+XLZy176aWXtGbNmrp37169fPmybtq0ieFLN7Fy5UoNCAjQvn376p49e6xrPE6ePKm9e/dWV1dX/fPPP/XEiRP6yy+/WM8LDAzU8PBwrrlxohuHA6anp+uVK1d0zZo1+u2332q1atW0YcOGWqNGDS1VqpTGx8drYmKitm/fXitWrKgNGjTQjh07apMmTfTZZ5+1rj985JFHNCwszFrv+vXr9ZlnntGyZctqnTp1HM74Xl+Xe/lExb/dvj///FObNm2qderU0ffee0/XrFljnbn89ttv1Wazaa1atbRw4cLaqlUrXbRokcMJpSlTpmilSpV09OjRum7dOu3cubO++OKLOmjQIF2/fr3x7cP/7sYD1b59+2ZZbujQoVqwYEF96KGH9KOPPrKuD1LNPMz2559/VpvNpmXLlrV6DG72urnNrUapqGYMdy5cuHCmkxDt27fX2rVrWyc97F5++WW9//77retdPv74Y/Xw8HCYeTAnvNeTJ0/W0qVLW70eixcv1ooVK1qB6NVXX9WSJUuqasbMc0eOHNFr165Z2zZo0CBt1qyZHj161GG9r7/+ulapUkVLlSql7u7u+sILL2TZc3L9b1JuCP3z58/XypUr69dff62qmfeRs2fPqre3t8O1UT/88IPabDZ95513VDXjc9+9e3cNDAzUr7/+Wp9++ml9++23Hdbz999/67fffqsjR440dp3Vv0HIyiH+6Wzb559/rrVr19YvvvhCz507px999JHWrVvXSvWTJk1ST09Phy/OPXv2OFz0t3HjRm3VqpWWLl1abTabPvnkkzf9gcrtIiMj1cfHx+EAz+7ixYv6+eefa1pamv7999969uxZPXHihL722mv60EMPWRMk4M661edn8+bNarPZNDg42PoiPnv2rBYtWlRHjRql6enpev78eZ08ebK+//77OmPGDB05cqQ2atRIW7Rooaqqy5YtU5vNpn/88Ye13tTU1Fz5GbrxQO6PP/7Qn3/+WS9fvmy1w7Vr1/T06dM6atQo69qHBQsWWJPD3OiXX37RkiVLas+ePR2GKKenp+uePXv09OnTevHiRX3rrbe0QoUKWrx4cR00aNBNh5/hzvg3PUUDBw7UJk2aWAeq6enp1nOXLl3q0JtsX75//3597rnnrH3Ovtw+lAv/zoEDB9TNzc0aTmUPsDNnztTAwEBrmKV9+QcffKA2m83qMTx37pwWL17cev7dZvXq1free+9Zv932/Wbr1q368MMPW9f5HDhwQB999FGrd2rHjh3q4+Ojvr6+2qhRI23SpIkWK1ZM33zzTVXNmASsVq1a1t8rVqywvntOnz6t69evzxXh6Z9cf1Klbt261vt1I/vxaGRkpI4cOVJLliypvr6+Gh4ertHR0dZ6zp49q61bt9bGjRtriRIl9Msvv7xj23I7CFl3scuXL2v37t2tmfzs7GOiV6xYoaoZX2oNGzbUBQsWqGpGN/ZHH32kbm5uGhYWpklJSbp9+3b18/PTefPmOay/ffv2WrduXVXN+HGKiYnRJUuWOIwPRmY7d+5Ud3d362zqzc7U7dq1S8PCwvS+++7TmjVr6pdffpllDyWyR1Y/auvXr9dBgwbpjBkz9OTJ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rmz1WFzf6zB79mz18vKyzsivXbtWS5cubd0j6bPPPtPu3bvrRx99xG0knOyfhl+98MIL2rFjR+ug9vp7ID333HNqs9m0TZs2+tVXX1m9K6rq8P83vtbu3bszPX63HtTfCdf31s2ePVuLFStm3fNSVXX8+PEaFhamx44ds5ZVqFBBe/bs6dAe/fv3V5vNptWrV9eRI0fe1muPGjVKx4wZ47Sbdl+8eFHfe+8967q7rK47S01N1UmTJmmRIkW0XLly2rBhQy1btqx1svp69n3oqaee0tatW1vX4Nq/444dO6Zt27bVpk2bqmrGZRuLFi3KNBlYbjzJdqNNmzZpp06dtG7dutYNqIcPH64NGjSw2uufJkRJSUnRli1bas+ePXXlypX63HPPqZeXl9psNp0wYcJNrx3MKQhZ2eyzzz5TNzc3rV27tkZFRem5c+f0vffeU39/f+3YsaOqZlwrcv0NE1esWKE2m806AImJibFuSqf6f0MKf/zxR61Zs6Z1Pyw7rlHAverGA+769eurp6enNc2u/WCkS5cuWr9+fYcel02bNmnx4sV1/Pjx1g0QT506pa+//rq+8MIL1kHijz/+eNMbVuYmWQ3HPHnypNavX1+9vb2tnoYbD77s793333+vNWrU0A8++EBVHc+Yv/fee1q0aFGHA+mSJUvqhAkTctXsWznJ999/r88++6wOGjRIt2/fbl3PW7FiRR08eLCqZtzU/ty5c9Zw2xUrVmjevHl1+/btDuuKiorSkSNH3rRH1O76YabIGAnz+++/a758+awTQ6qqDz/8sDWsb86cORoaGqo2m00jIiKsYW8JCQlarlw5/fLLL/WTTz5RLy8vffLJJ2869ND+OU5OTta///7baSc7li1bpj4+Ptb22etx5MgR64TZnj17tGbNmg7XyHbs2NHhZuf27bHvT19//bWWKVMm04gH1Yz77b388su5/pr1W33+hgwZot7e3tqzZ0/96KOPNCoqSlUzrv1/6KGHNDg4WDt27Kh9+vTRxx9/XBctWpRpHfbv+VdffVVtNps1WZJ9Mqp7ASErm/3yyy/auHHjTDdIGzJkiDWrX1JSkiYkJOjEiRO1fPny6uvrq56envrUU0+pasaO+NJLL6m/v79euXJF09LSrGE2TZo00fHjx1sHl7mt2xq5w+eff64tW7bUkJAQnTFjhjXl68yZM9XDw0NnzZqlqv/3A7xt2zbNkyePNSzJ/rmYOnWqenp6arNmzbRVq1bq6emp9evX18jIyHv+xsD/ix07dujTTz+t8+bN09KlS2uRIkX+8eDszJkz2rlzZ23VqpXD4z/++KOWKlXKOjC3XwvxTwfcyF43O6C6du2a9u/fX4sVK6Y9e/bUpk2bapkyZayTfvZ7MPr5+eljjz2mtWvXVj8/P+vMdnBwsNasWVPffvtt3bJli77++utavXp1HTp0KPcwu8HNDmg///xz9fb21rJly2qPHj3UZrNp165dVTXjdgXNmzfXSpUqqZeXlz7wwAM6cuTITNev7d69W++//35r5Muvv/6qTz75pI4YMeKuPKlh/x45duyYdujQQZ9++mnrsStXrmipUqWsWz/07t1bX3zxRVVV3bt3r44ZM0YLFiyotWrVsu7Bl9X6AwIC9OWXX7ZOCtzOpBm5UUJCgsMNlLdv3641atTIcuKnlJQUXb58ufbt21fHjx+vI0eO1DZt2mhAQIA1udGNk7wdPnxYv/76a+u34F5CyMpmqamp2r17d23VqpXDTtqlSxcNCAiwDhbHjRunderU0Y8//ljj4uJ03rx5WrBgQasr+8SJE+rj46OBgYHq7u6uoaGhmpCQ4HCBPpBTpaam3vRH7K233tLy5cvryJEj9e2339aGDRtqs2bNVDXjy7latWr66quvWuXt6ylVqpQOHTrUOnCxD1/Yvn27zp49W4cNG6a//fZbNm5VzpHVDHEpKSk6ZswYXbVqlXbr1k3btm2rhw8f1h9//FEbNWqkb731lqreejbF9957T6tUqaLHjh3ThIQEHTt2rNarV0979+7tMIwJd4/z58/r+vXrresffvjhB/X29rbO+P/99986YcIEdXV1tX7TIiMjdc2aNbp8+XL96aef9KmnntIGDRpoQkKCHjt2TIcOHapNmzZVPz8/DQwM1M8//9xp2+dMN5sk4VYH8Pb7YEZEROjVq1d1y5Yt2rFjRy1YsKAeO3ZM09PTtXXr1lq5cuVMM6OePHlSt27dqqoZw7jsM37erb2DNxuCN2HCBH3wwQet46HBgwdr8+bNrbJdu3bVMmXKaP369bVw4cLaqlUr/fzzz7MckqqqDs/r1q2bwxT319flbgyf2eX6993+nb5+/Xpt3Lix+vr6akhIiA4aNEhVM353bTabzp8/X1esWKGff/65btiwQffu3evwntnXs2vXLq1QoYI1zDw3IWTdAbNmzdKgoCDrDujz589XX19fHT16tKpmBKgCBQro3LlzrR10xIgRarPZHCat2L59u86aNeumZ2aAnCSrH9Mbx29v3bpVS5Ysad04UjVj+IjNZtOvvvpKVVWfeeYZbdu2rXU9gr03a/z48VqmTBnt2LGjBgQE6BNPPJFlPe6G2bGc5VbbHRcXp0FBQWqz2axeJ9WMi8b79OmjwcHBN32u/aAxKipKq1evrgUKFFB3d3etUaOGzps3L9e+33eLrO5ntXHjRm3YsKHmz59fW7dubU2X/vnnn6uPj4/D8+Pi4tTf31+nTJmS5fpHjRqltWrVchhudfbs2UwHvbm1d8C+/984KcOnn36qr7/+usPEINHR0Wqz2awTsqoZxwxeXl46depUVVWdNm2aVqtWzWGSkLi4OB02bJj269dPVVXffPNNh5kCr6/L3dAOt6rD+vXrtXbt2jp58mRNTEzUChUq6Pfff6+qGQfyM2fOVBcXF506darD5AhpaWl66NChTBNV2Pf/3DQc8HZnuLZfx/bHH39oYGCgDho0SHfs2KErVqzQkiVL6tixY1U14zPu4+OjNWvW1LCwMC1SpIjWrFnTup5527Ztev78ed21a5d269ZNW7VqddffsDo7ELLugP3792uzZs20YsWKWrx4cfX399eJEydaB4NxcXHq5eWl7777rqanp+sff/yhPXr00IoVK2pwcHCumqIW97aszgympqbqe++9p5UqVdJmzZo5XGO4YsUKffjhh/XQoUP6yiuv6P3336++vr763HPPWdcCzZs3T+vUqaPLli2z1qeaEdg+++wz7dChg86aNSvT5yi3nam8lSVLlmjv3r31gw8+0D///FNVM3qy5s+fry4uLrpx40aH8p988okGBARYy2/2HRUbG6tvvPGGvvnmmw7XneLucvHiRX344Yf1+eef10OHDmlMTIx1be/EiRO1fv36Vq+v/WCtW7du2rhxY1XNuD5m6dKlunbtWu3Vq5dWrFgxywN61dw9YcC6deu0VatWVkBQVf3tt9908+bN2r59e61QoYI2bdpUXV1dreGWkZGRDiea7J+1Z599VuvVq6eqGb2PI0eO1Dx58uiTTz6p4eHh6uvrq7Vr17ZORt1trt8P7N/Df/75p/bt21eDg4N1xIgR1onpM2fOaLdu3TQkJEQ/+OADfeaZZxyuEduxY4cWKVLEGj5o98UXX+igQYOs77Rb1eVek9WsivHx8VkGnfPnz+uBAwe0YsWKet9996lqxqQ19iGpqhm9oqVLl9YqVarovn37NC0tTS9duqTnz5/XI0eO6OnTp7V58+bWPcbCw8O1du3aWrBgQQ0LC7OGqeY2hKw75MUXX9SSJUvedNayYcOGqbe3t1asWFELFiyoI0eO1AsXLuT4mVWQu/ybH6sTJ05o+/bt9YsvvtAWLVro5MmTrQtgX3vtNU1JSdGPP/5YixYtqvny5dNHH31UFy5cmGk62LNnz2pwcLAOHDjwH8/I3g1nbJ3h+rPV9n/T0tJ0xYoVWqlSJS1Xrpx26dJFq1evrpUqVbKG8h06dEjvu+8+a3pd+5j5Xbt2acuWLfX555+3XoOhy86XmpqqCxYssIaNXT+7pp29x+T6obRvvvmmlilTJsuZIr///ntt0KCBTp8+3Xr+tWvX9JlnntEnn3zSugfjk08+qWXKlNEnnnhCf/jhh2ze0pzF/pn77bfftEqVKtY12mlpaVqkSBGtXLmyvvzyy1ZweOKJJ7R58+Z6/PhxjY6O1kaNGum4ceMc1jVmzBj18PBwmEH4+++/1xEjRmjPnj2zvGbyToaJW00Nfz37MO7o6Gh98MEH9dFHH9W3335b69Wrp8WKFbO2b9asWVquXDm12WzatGlT/emnnxy+zydNmqTe3t7avHlzffvttzU4OFjvv/9+HTlyZK4amnyz9/2XX37RPHnyWLcnsb/vixYt0jJlymi7du10+vTpVk9gixYttF+/fjp16lQtWbKkFi9eXDt16qQ///xzljcOPnv2rD700EPWyZWNGzfqqlWrcv3ssISsO2Tx4sVav359K2TdeA1KcnKy/vDDDzp9+nQ9fvy4s6oJGJPVRaxxcXHau3dvPX/+vCYkJKirq6vmyZPH4RqNGTNm6EMPPaQrV67UAwcO6IMPPqgvvfSSw3quXLmiY8eOtaYHf+aZZ7RDhw6ZbnBql1vPnN8YKm8MQu+++67Onj3b+vvKlSvq6+urb7zxhqpmfC89/fTTVo+F/X1MTk7Wt99+WwsVKqTDhg3TihUr6pgxYzgpdAdldS3PX3/9pU2bNs002UhiYqLDgVH//v21fv361tDzHj16WG1sL2dv66tXr2qXLl20SpUqGh0draoZtyUpV66cdY1FSkrKP/YWIEP79u31qaeesq4vevnllzVv3rwO34EbN27UgIAAXbhwoaamplr3jLN/vpKSkqwZBIcMGXLL13P2d9/Nrrc9deqUPvzww9ZQ1N69e2uDBg0cTqIFBgbqU089pQkJCRodHa2PPPKIBgcH68iRI9XHx0dbtGihq1atssqvW7dOhw4dqqGhoTpy5Mib/h7kBhs2bND33nvPIYQXKlRIn332Wa1fv77abDbds2eP/vzzz1q7dm0NCAiwZti9cuWK9uvXT202m4aGhupnn33mcN2afT+cO3euvvTSS9qhQwf18vLSNm3acPx6A0LWHXLy5El94oknMt1EEMiJbtYj9Ouvv1o3zs7Kzp071cfHx5p6d8CAAVq0aFH9448/rDInT57UsLAw7d+/v6qqRkREaNmyZXXp0qV6+vRpPXbsmI4ZM0YDAwN1w4YNqqoON93Mzew9CNcfUCcmJuqUKVM0ODhY27Ztq5999pl1j50DBw5oWlqanjp1SkeMGKEVKlRQm82mDz74oPWj+tVXX6mLi4s1+5+97ZOSknTs2LHatm1bnTRp0j05M9Td6J96IyZPnqxVqlSxDuJnzpypjRo1criWd8OGDRoUFGQNzZ00aZI1TCgrJ0+e1CZNmmiZMmU0KChIPTw8tH379lneHDS3TruelpZ2y6H99vdkzpw5WrduXeuat19++UW9vb2tm9/aBQcHa+/evfXq1at64MABDQgI0CpVqujrr7+ubdq00SFDhuj777+f5bDMOzkUOqtbPahmbFelSpWs/dDum2++0aCgIB00aJAOHz7cGhJYt25dHT58uKr+30H8smXLtESJEvrrr79qYmKiDhgwQOvXr6+qGb3s3bp105IlS2qVKlWs34Ib973cNGvshQsXdPjw4VqsWDEtU6aMPvroozp79my9fPmyLl++XG02m+bPn18HDhxonRT5+++/9dlnn9WyZcs6rOuDDz5QX1/fTPdaXbt2rU6ePFlTUlL0559/1kcffVT79u2r27Ztu2PbmZMQsu6gQYMGaUBAQJY3yAPuBbt27VKbzaarVq3SyMhIHTVqlMOsmpGRkVqpUiXr3iU//vij5smTR3fs2OFwZr5Lly7apk0bTU5O1osXL+pzzz2n5cuXtyZRaNCgga5YsSLTj+e9OLb+Rjc7YFi5cqXabDaHm2Zeu3ZNe/ToodWrV9dp06bp8OHDtW7duta4edWMC5zr16+voaGhOnfuXN2+fbvmzZvXulfJmTNnHO7Td/1BS245eLkbbd++XYcOHapdu3bVd9991/pMrVu3TuvUqaMTJkxQVdXVq1drjRo1dObMmdZzU1JStG3bttqhQwdNTEzU3377TQsVKpTpgD0qKsqahOHChQsaGRmp48ePt24hgqwdPXrUuhefnf2zcurUKa1Xr57DjKg1atTQAQMGOEwM8sYbb2hwcLB1/6E9e/boyJEj9aGHHtLevXtnCi/Odv78eV2zZo1DvWw2m44bN05feOEFLVasmB4+fFhXrlypAQEBWr58eT18+LCqZkwR3qVLFw0NDVVVdbgljbu7u37zzTeqmjG07cEHH7QCqmrGRA0//fSTVd7ubpnQ404aNWqUBgcH67fffquXL1/WEydOWJN+nD59Wj/77DO12WzWfevs78+HH36o5cqVs2aiVFU9fvy4hoaGarVq1XT27Nm6d+9enTBhgtapU0f79euXKyex+C8IWXfQ1q1bdfXq1bniQBD3tr/++kvHjh1r/aBeP036I488ol26dNFVq1Zp+fLlNSIiwnre0aNH1c3NzeoVSUlJ0dKlS+tLL73kcAbyqaee0hYtWlh/p6am6qlTp/Srr77K8ux5bnP9e3D9fanKlSun77zzjvXYokWLtHTp0tb4e9WMqZxtNps1cUinTp20efPm1sQUu3fv1oIFC1o3eL527Zp26dLllj2UyH72dl6zZo3WqVNH77vvPn3mmWd06tSpGhERYU2xfv78ee3evbs2bdrUem5ISIh2797dYSjWxIkTNTAw0DpAHTJkiJYoUUL79++vUVFROnr0aA0ODtYlS5bctD659bcsq546+6QNfn5+Ghoaqps2bcpUxt6GPXv21EcffdQ64fraa69p7dq1HWZR3bdvn3p7e1vXYv2butwp6enpumjRIq1du7Z6e3trcHDw/2vvzuOiqtc/gH9mWJU0YlEckE0EAsFkl1iC0AJECqk0yfVeLiRiXIS4BhdSES2zK2WySJZl4oaS5IaIWopSLIVewIUQF7wIiAIqwszz+4PfnBzF6nZN1Hne//hi5njO95wzc+Y85/t9ni+tWbOGrl69SkeOHCF1dXVSVVWl8ePH0/bt24mot1c0KChIKCcvX8/KlSvJ1NRUeEgk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",
      "text/plain": [
       "<Figure size 1000x1000 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.boxplot(figsize=(10,10), rot=20);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "f849bc72",
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.set_option('display.max_columns', 50)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "09f6340e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Age', ylabel='Count'>"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.histplot(df[\"Age\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "f91534d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Gender\n",
       "Male      7622\n",
       "Female    7378\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Gender\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "2f7a98c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.249\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Age', ylabel='Count'>"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(df[\"Hypertension\"].mean())\n",
    "sns.histplot(df[\"Hypertension\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "641960e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Hypertension', ylabel='Age'>"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.boxplot(x=df[\"Hypertension\"],y=df[\"Age\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "2294937a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.5029333333333333\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Hypertension', ylabel='Age'>"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(df[\"Heart Disease\"].mean())\n",
    "sns.histplot(df[\"Heart Disease\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "a0240e8d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Heart Disease', ylabel='Age'>"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.boxplot(x=df[\"Heart Disease\"],y=df[\"Age\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "963db780",
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
       "      <th>Hypertension</th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Heart Disease</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5607</td>\n",
       "      <td>1849</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5658</td>\n",
       "      <td>1886</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Hypertension      0     1\n",
       "Heart Disease            \n",
       "0              5607  1849\n",
       "1              5658  1886"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.crosstab(df[\"Heart Disease\"],df[\"Hypertension\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "87dc91e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Marital Status\n",
       "Single      5156\n",
       "Divorced    4980\n",
       "Married     4864\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Marital Status\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "242e7027",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Marital Status', ylabel='Age'>"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.boxplot(x=df[\"Marital Status\"],y=df[\"Age\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "544e6d5d",
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
       "      <th>Hypertension</th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Marital Status</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Divorced</th>\n",
       "      <td>3735</td>\n",
       "      <td>1245</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Married</th>\n",
       "      <td>3653</td>\n",
       "      <td>1211</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Single</th>\n",
       "      <td>3877</td>\n",
       "      <td>1279</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Hypertension       0     1\n",
       "Marital Status            \n",
       "Divorced        3735  1245\n",
       "Married         3653  1211\n",
       "Single          3877  1279"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.crosstab(df[\"Marital Status\"],df[\"Hypertension\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "5f2f267a",
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
       "      <th>Gender</th>\n",
       "      <th>Female</th>\n",
       "      <th>Male</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Marital Status</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Divorced</th>\n",
       "      <td>2429</td>\n",
       "      <td>2551</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Married</th>\n",
       "      <td>2439</td>\n",
       "      <td>2425</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Single</th>\n",
       "      <td>2510</td>\n",
       "      <td>2646</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Gender          Female  Male\n",
       "Marital Status              \n",
       "Divorced          2429  2551\n",
       "Married           2439  2425\n",
       "Single            2510  2646"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.crosstab(df[\"Marital Status\"],df[\"Gender\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "4ec57771",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Work Type\n",
       "Private           3863\n",
       "Self-employed     3855\n",
       "Government Job    3710\n",
       "Never Worked      3572\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Work Type\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "194e724b",
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
       "      <th>Work Type</th>\n",
       "      <th>Government Job</th>\n",
       "      <th>Never Worked</th>\n",
       "      <th>Private</th>\n",
       "      <th>Self-employed</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Marital Status</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Divorced</th>\n",
       "      <td>1229</td>\n",
       "      <td>1190</td>\n",
       "      <td>1315</td>\n",
       "      <td>1246</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Married</th>\n",
       "      <td>1234</td>\n",
       "      <td>1143</td>\n",
       "      <td>1243</td>\n",
       "      <td>1244</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Single</th>\n",
       "      <td>1247</td>\n",
       "      <td>1239</td>\n",
       "      <td>1305</td>\n",
       "      <td>1365</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Work Type       Government Job  Never Worked  Private  Self-employed\n",
       "Marital Status                                                      \n",
       "Divorced                  1229          1190     1315           1246\n",
       "Married                   1234          1143     1243           1244\n",
       "Single                    1247          1239     1305           1365"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.crosstab(df[\"Marital Status\"],df[\"Work Type\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "1188ccd1",
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
       "      <th>Work Type</th>\n",
       "      <th>Government Job</th>\n",
       "      <th>Never Worked</th>\n",
       "      <th>Private</th>\n",
       "      <th>Self-employed</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Gender</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Female</th>\n",
       "      <td>1812</td>\n",
       "      <td>1788</td>\n",
       "      <td>1895</td>\n",
       "      <td>1883</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Male</th>\n",
       "      <td>1898</td>\n",
       "      <td>1784</td>\n",
       "      <td>1968</td>\n",
       "      <td>1972</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Work Type  Government Job  Never Worked  Private  Self-employed\n",
       "Gender                                                         \n",
       "Female               1812          1788     1895           1883\n",
       "Male                 1898          1784     1968           1972"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.crosstab(df[\"Gender\"],df[\"Work Type\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "46dfbc57",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Residence Type\n",
       "Rural    7529\n",
       "Urban    7471\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Residence Type\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "00bebdd8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Marital Status', ylabel='Average Glucose Level'>"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.boxplot(x=df[\"Marital Status\"],y=df[\"Average Glucose Level\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "47de0667",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Marital Status', ylabel='Age'>"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.histplot(df[\"Average Glucose Level\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "2dbecf82",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Hypertension', ylabel='Average Glucose Level'>"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.boxplot(x=df[\"Hypertension\"],y=df[\"Average Glucose Level\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "eaabb0c4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Heart Disease', ylabel='Average Glucose Level'>"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.boxplot(x=df[\"Heart Disease\"],y=df[\"Average Glucose Level\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "0d487d09",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Heart Disease', ylabel='Average Glucose Level'>"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.histplot(df[\"Body Mass Index (BMI)\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "abb73d92",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Heart Disease', ylabel='Average Glucose Level'>"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.histplot(df[\"Body Mass Index (BMI)\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "3cba8d45",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Heart Disease', ylabel='Average Glucose Level'>"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.histplot(df[\"Body Mass Index (BMI)\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "c9cf4194",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Work Type', ylabel='Stress Levels'>"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.boxplot(x=df[\"Work Type\"],y=df[\"Stress Levels\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "34e29498",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Work Type', ylabel='Stress Levels'>"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.histplot(df[\"Stress Levels\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "35c2c976",
   "metadata": {},
   "outputs": [],
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
