# Controlling Smart Car Kit from RPi (communication)

The following code helps in communicating between Raspberry PI and Arduino. Through this we can control the smart car using Raspi

## 📽️ Demo Video

👉 *[[Demo video link here](https://youtu.be/1AZHrxAGies)]*

---

## 📌 Project Overview

This system provides a wireless communication and intelligent control method for operating a Smart Car Kit using a Raspberry Pi and an Arduino. The Raspberry Pi acts as the central controller, sending commands to the Arduino, which directly manages the motors and sensors of the car.

Through this setup, the Smart Car can be controlled remotely and efficiently, enabling flexible applications like navigation, obstacle avoidance, and autonomous driving experiments.

---

## ⚙️ Features

- 📡 Communication between Raspberry Pi and Arduino
- 🎮 Remote smart car control using Raspberry Pi as the main hub
- 🔄 Real-time command transmission with minimal delay

---

## 🧰 Technologies & Libraries

- **Python 3**
- **Arduino IDE** (for writing motor control logic)

---

## 🛠️ Hardware Components

| Component                    | Quantity |
|-----------------------------|----------|
| Raspberry Pi                | 1        |
| Arduino Car Kit             | 1        |


---

## 🧪 Working Principle

1. The Raspberry Pi sends directional commands (forward, backward, left, right, stop) to the Arduino
2. The Arduino receives these commands and translates them into motor control signals using a motor driver.
3. The Smart Car responds in real time, moving according to the received instructions.

---

## 👨‍💻 Authors

Developed by:

- **Anshul Dewangan**
- **Pratyaksh Lodhi**
- **Aaron David Don**
- **Joshua Benchamin**

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---

