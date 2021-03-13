# ComputerV1

A python polynomial equation solver.

### Requirements

Handle polynomial equations of degree <= 2.

No math functions/libraries allowed.

For a given equation display:
* Reduced form
* Degree
* Solution(s)
* Sign of the discriminant when it makes sense

#### Final Score 125/100


## Getting Started

First clone this repo to your machine.

```git clone https://github.com/dfinnis/ComputerV1.git```

Then run with equation as argument.

```python3 computor.py "0 * X^0 = 1 * X^1"```

<img src="https://github.com/dfinnis/ComputerV1/blob/master/img/example.png" width="640">

You can find some example equation files in the ```equations/``` folder.
You can also run an example file directly.

```python3 computor.py "$(< equations/1.txt)"```

<img src="https://github.com/dfinnis/ComputerV1/blob/master/img/file.png" width="640">

## Flags

### -n --natural

Using flag ```-n``` inputs in a natural form are accepted. This is much easier on the eye than the prescribed full format.

<img src="https://github.com/dfinnis/ComputerV1/blob/master/img/natural.png" width="640">

### -d --decimal

Flag ```-d DECIMAL_PLACES``` sets number of decimal places for displayed solution.

<img src="https://github.com/dfinnis/ComputerV1/blob/master/img/decimal.png" width="640">

### -s --steps

Flag ```-s``` displays intemediate steps.

First the left side of the equation is read (everything left of "=") and reduced to power 0, 1 and 2. Then the right side of the equation is read, reduced, and subtracted from the left, creating the final reduced form.

<img src="https://github.com/dfinnis/ComputerV1/blob/master/img/steps.png" width="640">

## Dependencies

Python 3.9.1

(no requirements.txt required)
