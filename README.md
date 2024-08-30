# predictive_battery_health_monitoring
Predictive Battery Health Monitoring with AI on Edge. 

### Dataset festures

To monitor of battery health the following features where identified. 

Due to the lack of available open data about batteries, in this project, the data will be generated to simulate different conditions and refelct its influence on the state of health (SoH). 

The table below summarizes the features that corrolate with the SoH. 

| Data Feature               | True Value Range                         | Explanation                                                                                     |
|---------------------------|------------------------------------------|-------------------------------------------------------------------------------------------------|
| **Charging Frequency**     | 1 to 3 times per day                    | Charging frequency can vary widely depending on user habits. Many users charge overnight, while others may charge multiple times throughout the day. |
| **Charging Duration**      | 30 minutes to 12 hours                  | Charging duration depends on the charging method. Level 1 chargers may take longer (up to 12 hours), while Level 2 chargers can typically charge a vehicle in about 4 to 8 hours. Fast chargers can charge a battery to about 80% in around 30 minutes to 1 hour. |
| **Ambient Temperature**    | -20°C to 50°C (-4°F to 122°F)          | Ambient temperature significantly affects battery performance. EV batteries are designed to operate within this range, but extreme temperatures can lead to reduced efficiency and capacity. |
| **Acceleration**           | 0 to 3 g                                 | Typical acceleration rates for electric vehicles can vary, with aggressive driving possibly reaching up to 3 g in rapid acceleration scenarios. |
| **Braking**                | 0 to 1 g                                 | Deceleration rates during braking typically do not exceed 1 g in normal driving conditions. |
| **Speed**                  | 0 to 200 km | 0 to 200 km/h (0 to 124 mph)            | Maximum speeds vary by vehicle, but most electric vehicles can reach speeds up to 200 km/h on highways. |
| **Remaining Battery Cycles**| 300 to 1,500 cycles                     | The number of cycles an EV battery can undergo before significant degradation varies by battery chemistry and usage. Most lithium-ion batteries are rated for approximately 1,000 cycles, but some can last up to 1,500 cycles with proper management. |
