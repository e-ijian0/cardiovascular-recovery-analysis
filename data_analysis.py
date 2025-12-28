# Main script for physiological data analysis.
import math

def calculate_recovery_slope(bp_data, time_stamps):
    """
    Calculate the slope of linear regression of blood pressure over time.
    
    Parameters:
    -----------
    bp_data : list of float or int
        Systolic blood pressure readings.
    time_stamps : list of float or int
        Corresponding time stamps in minutes after stressor.
        
    Returns:
    --------
    float
        Slope of the linear regression line (change in BP per minute).
        Negative slope indicates recovery (BP decreasing over time).
        
    Raises:
    -------
    ValueError
        If lengths of bp_data and time_stamps don't match,
        or if there are fewer than 2 data points,
        or if time variance is zero (all times identical).
    """
    if len(bp_data) != len(time_stamps):
        raise ValueError("bp_data and time_stamps must have same length")
    n = len(bp_data)
    if n < 2:
        raise ValueError("At least 2 data points required for slope calculation")
    
    # Compute means
    mean_x = sum(time_stamps) / n
    mean_y = sum(bp_data) / n
    
    # Compute covariance and variance
    cov = sum((x - mean_x) * (y - mean_y) for x, y in zip(time_stamps, bp_data))
    var_x = sum((x - mean_x) ** 2 for x in time_stamps)
    
    if var_x == 0:
        raise ValueError("Time stamps have zero variance (all identical), slope undefined")
    
    slope = cov / var_x
    return slope