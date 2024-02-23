#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 19:18:03 2024

@author: Anukriti Baijal
"""

""" Import important libraries for data extraction and manipulation """
import pandas as pd 

def clean(df, a, col):
    """
    Cleaning the column by removing of the specified character/string

    Parameters
    ----------
    df : Dataframe containing the column to be cleaned
    a : String/Character to remove
    col : The column to be cleaned
    
    Returns
    -------
    Column with clean values 
    
    """
    df[col]=df[col].str.replace(a, ' ')
    return df[col]

def convert_date_time(df, a, col):
    """
    Converting the contents of the specified column into correct date or time format

    Parameters
    ----------
    df : Dataframe containing the column to be converted
    a : Specific form (date or time) to be converted to
    col : The column to be converted

    Returns
    -------
    Column with correct converted form

    """
    if a=="date":
        df[col]=pd.to_datetime(df[col], format='%Y-%m-%d').dt.date
    else:
        df[col]=pd.to_datetime(df[col], format='%H:%M:%S').dt.time
    
    return df[col]

def cc_provider(df, col):
    """
    Extracting the first digit of the credit card number and determining the provider:
    2 or 5: Mastercard
    3: American Express
    4: Visa
    6: Discover

    Parameters
    ----------
    df : Dataframe containing the column with credit card numbers
    col : Column contaning credit card numbers

    Returns
    -------
    Column with credit card provider names.

    """
    df['cc_provider'] = df[col].astype(str).str[0]
    replace_dic={'1':"Other",'2':"Mastercard", '3':"American Express",'4':"Visa", '5':"Mastercard", '6':"Discover"}
    df['cc_provider']=df['cc_provider'].replace(replace_dic)
    
    return df['cc_provider']

def age_group(a):
    """
    Dividing the contents of the specified column into different age groups
    Group 1: 0-18 years
    Group 2: 19-25 years
    Group 3: 26-40 years
    Group 4: 40-65 years
    Group 5: 65+ years

    Parameters
    ----------
    a : Age of the customer

    Returns
    -------
    Age group of the customer

    """
    if a<=18:
        return '0-18 years'
    elif a>18 and a<=25:
        return '19-25 years'
    elif a>25 and a<=40:
        return '26-40 years'
    elif a>40 and a<=65:
        return '41-65 years'
    else:
        return '65+ years'
