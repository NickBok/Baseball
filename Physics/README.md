# **Drag Coef**
*Author: Declan Costello*

## **Project Overview**

Inspired by ["Simplified Models for the Drag Coefficient of a Pitched Baseball" by David Kagan & Alan M. Nathan](http://baseball.physics.illinois.edu/DragTPTMay2014.pdf), this project observes how tempurature, humidity, and air pressure affect the drag coef. With an interest in hitting mechanics and atmospheric influences, the primary aspiration is to contribute meaningful insights to the baseball community.

<table>
<tbody>
  <tr>
    <td>
      <a href="https://github.com/dec1costello/Baseball/blob/main/Physics/Coefficient_of_a_Pitched_Baseball.ipynb">
        <img src="https://github.com/dec1costello/Baseball/assets/79241861/e7d22b62-a499-4bb9-ace4-9160067273bb" />
      </a>
    </td>
    <td>
      <a href="https://github.com/dec1costello/Baseball/blob/main/Physics/Coefficient_of_a_Pitched_Baseball.ipynb">
        <img src="https://github.com/dec1costello/Baseball/assets/79241861/0ff2de04-7370-4b1e-bde4-a3c8549873b1" alt="WOBA Heatmap" />
      </a>
    </td>
</tr>
</tbody>
</table>

## **Task List (TODO)**

- Integrate Humidor Stadium data, humidity, and [temperature](http://baseball.physics.illinois.edu/HRProbTemp.pdf) during games

import math

def calculate_spin_components(spin_axis_degrees, spin_rate_rpm):
    # Convert spin axis to radians for trigonometric functions
    spin_axis_radians = math.radians(spin_axis_degrees)

    # Calculate the gyro spin, which is parallel to the direction of travel
    gyro_spin = spin_rate_rpm * math.sin(spin_axis_radians)

    # Calculate the Magnus (transversal) spin, which is perpendicular to the direction of travel
    magnus_spin = spin_rate_rpm * math.cos(spin_axis_radians)

    # Calculate the backspin and sidespin components of the Magnus Spin
    # Assuming spin_axis_degrees is the angle from the horizontal plane
    # backspin is positive when the axis tilts upwards, negative for topspin
    backspin = magnus_spin * math.cos(spin_axis_radians)
    sidespin = magnus_spin * math.sin(spin_axis_radians)

    # 'topspin' is just the negative of backspin in this context, as it would be represented
    # by a negative angle for the spin axis
    topspin = -backspin if spin_axis_degrees < 0 else 0

    # Adjust backspin to be zero if the spin axis indicates topspin
    backspin = backspin if spin_axis_degrees >= 0 else 0

    return {
        'Gyro Spin': gyro_spin,
        'Magnus Spin (Transversal Spin)': magnus_spin,
        'Backspin': backspin,
        'Topspin': topspin,
        'Sidespin': sidespin
    }

# Example usage:
spin_axis = 45  # Spin axis in degrees from the horizontal
spin_rate = 1800  # Spin rate in rpm
spin_components = calculate_spin_components(spin_axis, spin_rate)

for component, value in spin_components.items():
    print(f"{component}: {value:.2f} rpm")

