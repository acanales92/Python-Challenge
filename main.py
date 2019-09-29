{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "\n",
      "----------------------------\n",
      "\n",
      "Total Months : 86\n",
      "Total: $ 38382578\n",
      "Average Change: $ -2315.12\n",
      "Greatest Increase in Profits: Feb-2012 : ($ 1926159)\n",
      "Greatest Decrease in Profits: Sep-2013 : ($ -2196167)\n"
     ]
    }
   ],
   "source": [
    "# First we'll import the os module\n",
    "# This will allow us to create file paths across operating systems\n",
    "import os\n",
    "\n",
    "# Import module for reading CSV files\n",
    "import csv\n",
    "\n",
    "#creating a path to access the csv file\n",
    "PyBank = os.path.join('/Users/Areli','Desktop','Python-Challenge','PyBank','budget_data.csv')\n",
    "#creating a path to createt a txt file\n",
    "file_to_output = os.path.join('/Users/Areli','Desktop','Python-Challenge','PyBank','PyBankAnalysis.txt')\n",
    "\n",
    "#Variables\n",
    "total_num_of_months = 0\n",
    "Total = 0\n",
    "p_revenue = 867884\n",
    "r_change = 0\n",
    "g_increase = 0\n",
    "g_decrease = 0\n",
    "Avaerage_Change = 0\n",
    "Total_change = 0\n",
    "\n",
    "#Open and read CSV file\n",
    "with open(PyBank, newline='') as csvfile:\n",
    "     csvreader = csv.reader(csvfile, delimiter=',')\n",
    "     #print(csvreader)\n",
    "     csv_header = next(csvreader)\n",
    "     print(f'Financial Analysis'+'\\n')\n",
    "     print(f'----------------------------'+'\\n')\n",
    "     for i in csvreader:\n",
    "         #getting the total number of months and overall revenue\n",
    "         month = i[0]\n",
    "         total_num_of_months = total_num_of_months + 1\n",
    "         total_net_amount = i[1]\n",
    "         t_net_amount = int(total_net_amount)\n",
    "         Total += int(total_net_amount)\n",
    "            \n",
    "         #Calculating the change btwn total net and previous rev\n",
    "         r_change =  t_net_amount - p_revenue\n",
    "            \n",
    "         #Calculating greatest increase in profits\n",
    "         if g_increase < r_change:\n",
    "            g_increase = r_change\n",
    "            g_increaseDate = month\n",
    "            \n",
    "         #Calcualting greatest decrease in profits\n",
    "         if g_decrease > r_change:\n",
    "            g_decrease = r_change\n",
    "            g_decreaseDate = month\n",
    "         #Once it loops, the new value is p_revenue\n",
    "         p_revenue = t_net_amount  \n",
    "         \n",
    "        #calculating the average\n",
    "         Total_change = Total_change + r_change\n",
    "         \n",
    "    #Calcualting the average change\n",
    "Average_change =  Total_change / (amount - 1)\n",
    "Average_Change = round(Average_change,2)  \n",
    "\n",
    "## Display Output Results in Python ##      \n",
    "\n",
    "print(f'Total Months : {total_num_of_months}')\n",
    "#The total net amount of \"Profit/Losses\" over the entire period\n",
    "print(f'Total: $ {Total}')\n",
    "#average change\n",
    "print(f'Average Change: $ {Average_Change}')\n",
    "# Greatest increase in profit\n",
    "print(f'Greatest Increase in Profits: {g_increaseDate} : ($ {g_increase})')\n",
    "# Greatest increase in profit\n",
    "print(f'Greatest Decrease in Profits: {g_decreaseDate} : ($ {g_decrease})')\n",
    "\n",
    "#printing a txt file\n",
    "with open(file_to_output,'w') as outputfile:\n",
    "        outputfile.write(f'Financial Analysis'+'\\n')\n",
    "        outputfile.write(f'----------------------------'+'\\n')\n",
    "        outputfile.write(f'Total Months:{total_num_of_months}' +'\\n') \n",
    "        outputfile.write(f'Total : $ {Total}' +'\\n')\n",
    "        outputfile.write(f'Average  Change: $ {Average_Change}'+'\\n')\n",
    "        outputfile.write(f'Greatest Increase in Profits: {g_increaseDate} : ($ {g_increase})'+'\\n')\n",
    "        outputfile.write(f'Greatest Decrease in Profits: {g_decreaseDate} : ($ {g_decrease})'+'\\n')\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
