# predictive_battery_health_monitoring
Predictive Battery Health Monitoring with AI on Edge. 

# Synthetic Battery Data Generator

This project generates synthetic data simulating the State of Health (SOH) degradation of electric vehicle batteries over time. The data is created to mimic real-world scenarios with various usage patterns and charging behaviors.

## Dataset Description

The generated datasets simulate battery performance over a three-year period, with daily entries. Each dataset represents a different combination of usage frequency and charging behavior.

### File Naming Convention

Files are named according to the pattern: `{usage}_usage_{charging}_charging_battery_data.csv`

Where:
- `{usage}` can be: low, normal, or high
- `{charging}` can be: optimal, full, frequent_top_ups, or deep_discharge

### Data Fields

Each CSV file contains the following columns:

1. **Date**: The date of the entry (daily frequency)
2. **Temperature**: Simulated ambient temperature in Celsius
3. **Charge_Start**: Starting charge level for the day (%)
4. **Charge_End**: Ending charge level for the day (%)
5. **Daily_Mileage**: Simulated daily driving distance
6. **Daily_Cycles**: Number of charge cycles completed in the day
7. **Total_Cycles**: Cumulative number of charge cycles
8. **SOH**: State of Health of the battery (%)

### Scenarios

The data is generated for six different scenarios:

1. Normal usage, optimal charging
2. Normal usage, full charging
3. Normal usage, frequent top-ups
4. Normal usage, deep discharge
5. High usage, optimal charging
6. Low usage, optimal charging

### Data Generation Parameters

- **Initial SOH**: 100%
- **Minimum SOH**: 70%
- **Temperature Ranges**:
  - Winter: -5°C to 10°C
  - Spring: 5°C to 20°C
  - Summer: 15°C to 35°C
  - Fall: 0°C to 25°C
  - Extreme events (5% chance): -20°C to -10°C or 40°C to 50°C
- **Usage Factors**:
  - Low: 0.5
  - Normal: 1.0
  - High: 1.5
- **Charging Behaviors**:
  - Optimal: 20% to 80%
  - Full: 10% to 100%
  - Frequent top-ups: 60% to 80%
  - Deep discharge: 5% to 95%

### SOH Degradation Factors

The SOH degradation is calculated based on:
- Base degradation rate
- Temperature effects
- Cycling effects
- Charging behavior
- Battery age

## Usage

This synthetic data can be used for:
- Developing and testing battery management systems
- Training machine learning models for SOH prediction
- Analyzing the impact of different usage patterns on battery life
- Simulating various scenarios for electric vehicle fleet management

## Limitations

- This is synthetic data and may not perfectly represent real-world battery behavior
- The degradation model is simplified and does not account for all factors affecting battery life
- Extreme scenarios or edge cases may not be fully represented

