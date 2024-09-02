import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def simulate_battery_data(start_date, end_date, initial_soh=100, usage_frequency='normal', charging_behavior='optimal'):
    start_date = pd.Timestamp(start_date)
    end_date = pd.Timestamp(end_date)
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    data = []
    soh = initial_soh
    total_cycles = 0
    accumulated_charge = 0
    
    usage_factors = {'low': 0.5, 'normal': 1.0, 'high': 1.5}
    usage_factor = usage_factors[usage_frequency]
    
    charging_behaviors = {
        'optimal': (20, 80),
        'full': (10, 100),
        'frequent_top_ups': (60, 80),
        'deep_discharge': (5, 95)
    }
    
    for date in date_range:
        # Temperature simulation with occasional extreme events
        season = (date.month % 12 + 3) // 3
        if season == 1:  # Winter
            temp = random.uniform(-5, 10)
        elif season == 2:  # Spring
            temp = random.uniform(5, 20)
        elif season == 3:  # Summer
            temp = random.uniform(15, 35)
        else:  # Fall
            temp = random.uniform(0, 25)
        
        if random.random() < 0.05:  # 5% chance of an extreme temperature event
            temp = random.choice([random.uniform(-20, -10), random.uniform(40, 50)])
        
        # Charging behavior
        charge_start, charge_end = charging_behaviors[charging_behavior]
        
        # Occasional full charge for 'optimal' and 'frequent_top_ups'
        if charging_behavior in ['optimal', 'frequent_top_ups'] and random.random() < 0.1:
            charge_end = 100
        
        # Driving behavior (daily mileage)
        mileage = random.uniform(30, 100) * usage_factor
        
        # Calculate cycles
        charge_amount = charge_end - charge_start
        accumulated_charge += charge_amount
        daily_cycles = accumulated_charge // 100  # Integer division
        accumulated_charge = accumulated_charge % 100  # Remaining charge
        
        total_cycles += daily_cycles
        
        # Calculate SOH degradation
        base_degradation = 0.005 * usage_factor
        
        # Temperature effect
        temp_factor = 1 + 0.1 * (abs(temp - 25) / 25)
        
        # Cycle effect
        cycle_factor = 1 + 0.05 * (total_cycles / 500)
        
        # Charging behavior effect
        if charging_behavior == 'full':
            charging_factor = 1.2  # More degradation for frequent full charges
        elif charging_behavior == 'deep_discharge':
            charging_factor = 1.3  # Even more degradation for deep discharges
        else:
            charging_factor = 1.0
        
        # Age effect
        days_since_start = (date - start_date).days
        age_factor = 1 + 0.1 * (days_since_start / 365)
        
        soh_degradation = base_degradation * temp_factor * cycle_factor * charging_factor * age_factor
        
        soh -= soh_degradation
        soh = max(soh, 70)  # Assuming minimum SOH of 70%
        
        data.append({
            'Date': date,
            'Temperature': temp,
            'Charge_Start': charge_start,
            'Charge_End': charge_end,
            'Daily_Mileage': mileage,
            'Daily_Cycles': daily_cycles,
            'Total_Cycles': total_cycles,
            'SOH': soh
        })
    
    return pd.DataFrame(data)

# Generate data for the past three years
end_date = pd.Timestamp.now().date()
start_date = end_date - pd.Timedelta(days=3*365)

# Simulate data for different scenarios
scenarios = [
    ('normal', 'optimal'),
    ('normal', 'full'),
    ('normal', 'frequent_top_ups'),
    ('normal', 'deep_discharge'),
    ('high', 'optimal'),
    ('low', 'optimal')
]

for usage, charging in scenarios:
    df = simulate_battery_data(start_date, end_date, usage_frequency=usage, charging_behavior=charging)
    print(f"\n{usage.capitalize()} Usage, {charging.replace('_', ' ').capitalize()} Charging Scenario:")
    print(df[['Temperature', 'Charge_Start', 'Charge_End', 'Total_Cycles', 'SOH']].describe())
    df.to_csv(f'{usage}_usage_{charging}_charging_battery_data.csv', index=False)