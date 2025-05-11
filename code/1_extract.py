import pandas as pd
import numpy as np
import streamlit as st
import pandaslib as pl
from typing import Dict

def fetch_and_process_survey_data() -> Dict[str, pd.DataFrame]:
    """
    Fetches survey data and cost of living information, then processes and caches it.
    
    Returns:
        Dict[str, pd.DataFrame]: Dictionary containing processed DataFrames with keys:
                                - 'survey_data': Main survey responses
                                - 'cost_of_living': Dictionary of DataFrames by year
                                - 'state_reference': State reference table
    """
    # intitializing storage for processed data
    processed_data = {
        'survey_data': None,
        'cost_of_living': {},
        'state_reference': None
    }
    
    # configuring for data sources
    survey_source = 'https://docs.google.com/spreadsheets/d/1IPS5dBSGtwYVbjsfbaMCYIWnOuRmJcbequohNxCyGVw/export?resourcekey=&gid=1625408792&format=csv'
    state_ref_source = 'https://docs.google.com/spreadsheets/d/14wvnQygIX1eCVo7H5B7a96W1v5VCg6Q9yeRoESF6epw/export?format=csv'
    col_base_url = 'https://www.numbeo.com/cost-of-living/rankings.jsp?title={year}&displayColumn=0'
    
    # processing survey data
    try:
        response_data = pd.read_csv(survey_source)
        response_data['year'] = response_data['Timestamp'].apply(pl.extract_year_mdy)
        response_data.to_csv('cache/survey_responses.csv', index=False)
        processed_data['survey_data'] = response_data
        
        # getting unique years for cost of living data
        unique_years = response_data['year'].unique()
        
        # getting cost of living data for each year
        for yr in unique_years:
            try:
                col_tables = pd.read_html(col_base_url.format(year=yr))
                living_cost_df = col_tables[1].copy()
                living_cost_df['year'] = yr
                living_cost_df.to_csv(f'cache/living_cost_{yr}.csv', index=False)
                processed_data['cost_of_living'][str(yr)] = living_cost_df
            except Exception as e:
                st.warning(f"Failed to fetch cost of living data for {yr}: {str(e)}")
        
        # processing state reference data
        state_data = pd.read_csv(state_ref_source)
        state_data.to_csv('cache/state_reference.csv', index=False)
        processed_data['state_reference'] = state_data
        
    except Exception as e:
        st.error(f"Error in data processing pipeline: {str(e)}")
        raise
    
    return processed_data


fetch_and_process_survey_data()