## **Part 2, [Feature Engineering](https://nbviewer.org/github/dec1costello/Baseball/blob/main/Distance-Predictor/Distance-Predictor-Part-2.ipynb)**

In Parts 2, I start to feature engineer to help understand, clean, and refine the dataset. It guides model choice and assumption validation, while also revealing insights through visualization. By addressing data quality and understanding patterns early, here I establish a strong foundation for the rest of my project.

# Part 2 - Feature Engineering Ideas:
- Add [My Custom Park Factors](https://github.com/dec1costello/Baseball/tree/main/Stadiums)
- [Temp and Humidity](https://towardsdatascience.com/getting-weather-data-in-3-easy-steps-8dc10cc5c859)
- Wind
- Player height, weight, throwing arm
- Hang time
- Use plate_x not pfx_x
- [Player max la arch](https://drive.google.com/file/d/1fC974yEShTAJ6PXWgbamLlriaFUzjf1r/view)
- At bats with contact per person
- HR per player per at bat contact
- Barrel per he per person at bat contact
- Day / Night Game
- Starting pitcher ERA
- [Redo barrel cassifications](https://x.com/JonPgh/status/1706726176973373637?s=20)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data generation
np.random.seed(42)
num_rows = 10000

launch_angle = np.random.randint(-100, 101, num_rows)
launch_speed = np.random.randint(0, 131, num_rows)

df = pd.DataFrame({
    'launch_angle': launch_angle,
    'launch_speed': launch_speed
})

# Define hit type regions based on the provided scatter plot
# Define hit type regions based on the provided scatter plot
def classify_hit(row):
    x = row['launch_speed'] # Launch Speed (mph)
    y = row['launch_angle'] # Launch Angle (degrees)

    # Weak (Red)
    if x < 60:
        return 'Weak'
    
    # Barrel (Yellow)
    elif y > x - 60 and y < x - 40:
        return 'Barrel'
    
    # Under (Purple)
    elif y > x - 80 and y <= x - 60:
        return 'Under'
    
    # Flare (Blue)
    elif y > 0 and y < x/2 - 20:
        return 'Flare'
    
    # Topped (Green)
    elif y <= 0 and y > -x/2 + 10:
        return 'Topped'
    
    # Solid (Orange)
    else:
        return 'Solid'


df['hit_type'] = df.apply(classify_hit, axis=1)

colors = {
    'Weak': 'red',
    'Flare': 'blue',
    'Topped': 'green',
    'Solid': 'orange',
    'Under': 'purple',
    'Barrel': 'yellow'
}

plt.scatter(df['launch_speed'], df['launch_angle'], c=df['hit_type'].apply(lambda x: colors[x]), s=20)
plt.xlabel('Launch Speed (mph)')
plt.ylabel('Launch Angle (degrees)')
plt.title('Launch Speed vs Launch Angle')
plt.show()
