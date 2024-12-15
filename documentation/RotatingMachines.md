In **rotary systems condition monitoring**, different fault conditions in rotating machinery (such as bearings, gears, and shafts) manifest as characteristic frequencies in vibration data. By analyzing the vibration signal in the frequency domain (using techniques like **FFT** or **STFT**), it's possible to identify specific fault types based on the frequency components.

Here are some common fault types in rotary systems and their associated characteristic frequencies:

### **1. Bearing Faults**

Bearing faults are often identified by specific fault frequencies that correspond to the geometry and operational characteristics of the bearing.

- **Ball Pass Frequency of Inner Race (BPFI)**:
  - **Formula**: 
    $$BPFI = \frac{N}{2} \left( 1 + \frac{d}{D} \right) f_r$$
    - \(N\) = Number of balls
    - \(d\) = Diameter of the ball
    - \(D\) = Pitch diameter of the bearing
    - \(f_r\) = Shaft rotational frequency
  - **Frequency Range**: Typically found in the high-frequency range (a few kHz) depending on the shaft speed and bearing design.
  
- **Ball Pass Frequency of Outer Race (BPFI)**:
  - **Formula**:
    $$BPFI = \frac{N}{2} \left( 1 - \frac{d}{D} \right) f_r
  - **Frequency Range**: Found in a lower frequency range compared to BPFI.

- **Fundamental Train Frequency (FTF)**:
  - **Formula**:
    $$FTF = \frac{f_r}{2} \left( 1 - \frac{d}{D} \right)$$
  - **Frequency Range**: Typically a lower frequency range and can overlap with other system vibrations.

- **Harmonics**:
  - Bearing faults can generate harmonic frequencies at multiples of the above fault frequencies.

---

### **2. Gear Faults**

- **Mesh Frequency (MF)**:
  - **Formula**:
    $$MF = \text{Number of Teeth} \times f_r$$

  - **Frequency Range**: Found in a range that depends on the number of teeth and the shaft speed. Typically, meshing frequencies fall within medium-frequency ranges (hundreds of Hz to a few kHz).

- **Sideband Frequencies**:
  - Often, you will observe sidebands around mesh frequencies in case of gear tooth wear or damage. These sidebands occur due to modulation caused by tooth defects.

- **Harmonics of Mesh Frequency**:
  - Gear defects also produce harmonics of the mesh frequency, especially when there are misalignments or cracks in the teeth.

---

### **3. Shaft/Rotational Faults**

- **Shaft Speed (f_r)**:
  - The fundamental frequency of shaft rotation is the **shaft rotational frequency** (\(f_r\)).
  - **Formula**: 
    
    $$f_r = \frac{\text{Shaft RPM}}{60}$$
    
  - **Frequency Range**: Typically in the low-frequency range (up to a few Hz for high-speed machines), but this can vary depending on the system speed.

- **Harmonics of Shaft Speed**:
  - If there is a problem with the alignment or balancing of the shaft, harmonics of the shaft speed may appear at multiples of \(f_r\), indicating issues like imbalance, misalignment, or looseness.

---

### **4. Imbalance and Misalignment**

- **Imbalance**:
  - Imbalance can cause a peak at the shaft rotational frequency \(f_r\), and its harmonics. The **2x** and **3x** harmonics are often visible in the frequency spectrum for severe imbalance.

- **Misalignment**:
  - Misalignment can also produce sidebands around the rotational frequency and its harmonics. Misalignment in gears or shafts causes the system to operate in a non-sinusoidal manner, creating distinct frequency patterns.

---

### **5. Looseness in Rotary Equipment**

- **Looseness**:
  - Mechanical looseness in bearings, couplings, or other parts of the system may generate a low-frequency vibration. This can appear around the **fundamental shaft frequency** and its harmonics.
  
---

### **6. Cavitation in Pumps and Motors**

- **Cavitation Frequencies**:
  - Cavitation (in fluid systems such as pumps or turbines) often creates high-frequency noise due to the formation and collapse of bubbles in the fluid.
  - Frequencies related to the pump’s rotation speed or blade frequency may appear in the spectrum.

---

### **Summary Table**

| Fault Type                        | Frequency Indicator                           | Frequency Range             |
|-----------------------------------|-----------------------------------------------|-----------------------------|
| **Ball Pass Frequency (Inner Race)** | $$BPFI = \frac{N}{2} \left( 1 + \frac{d}{D} \right) f_r $$ | High frequency (kHz range)  |
| **Ball Pass Frequency (Outer Race)** | $$BPFI = \frac{N}{2} \left( 1 - \frac{d}{D} \right) f_r $$ | Medium-high frequency       |
| **Fundamental Train Frequency (FTF)** | $$FTF = \frac{f_r}{2} \left( 1 - \frac{d}{D} \right) \$$ | Low frequency               |
| **Gear Mesh Frequency (MF)**       | MF = Number of Teeth × \(f_r\)                | Medium frequency            |
| **Harmonics of Mesh Frequency**   | Harmonics of MF                              | Medium-high frequency       |
| **Shaft Rotation Frequency (f_r)** | $$f_r = \frac{\text{Shaft RPM}}{60}$$         | Low frequency               |
| **Harmonics of Shaft Speed**      | \(f_r, 2f_r, 3f_r, \dots\)                   | Low-medium frequency        |
| **Imbalance Frequency**           | \(f_r\), \(2f_r\), \(3f_r\), \dots           | Low-medium frequency        |
| **Misalignment Frequency**        | Sidebands around \(f_r\) and its harmonics   | Low-medium frequency        |
| **Cavitation Frequency**          | Harmonics of pump speed                      | High frequency (kHz range)  |

---

### **Key Points:**
- **Low frequencies** (< 1 kHz) are often associated with problems in shaft rotation, imbalance, and misalignment.
- **Medium frequencies** (1 kHz - 10 kHz) are common for bearing and gear fault diagnostics.
- **High frequencies** (> 10 kHz) often relate to high-speed bearing damage or cavitation.

By analyzing these frequencies, one can diagnose the **condition of the rotary equipment** and perform **predictive maintenance** to avoid catastrophic failures.