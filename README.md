# Sankey Diagram

**Author:** Dao Bui  
**Date Created:** 05/20/2025  

## 📌 Description

This project creates an animated Sankey diagram from a data file, visually representing the distribution of values across categories using smooth, colored flows and proportional bars. It uses the `graphics.py` library to render the visualization in a GUI and saves the output as both PDF and PostScript files.

---

## 💡 Features

- Reads structured input from a `.txt` file
- Animated flow connectors with gradient coloring
- Automatically scales diagram based on values
- Displays source and destination labels
- Exports visualization to `.ps` and `.pdf` formats

---

## 📁 Input File Format

The input text file should follow this format:

```
<empty line>
<Diagram Title>
<Source Label>
Category1, Value1
Category2, Value2
...
```

**Example:**
```
  
California Electricity Flow
Total Electricity (TWh)
Residential, 200
Commercial, 150
Industrial, 100
```

---

## ▶️ How to Run

1. Make sure you have the `graphics.py` module in your project directory.
2. Run the script using Python 3:
   ```bash
   python sankey_diagram.py
   ```
3. Enter the name of your data file when prompted.
4. The Sankey diagram will appear in a window.
5. The output will be saved as both `.ps` and `.pdf`.

---

## 🧩 Dependencies

- Python Standard Library:
  - `math`
  - `random`
- [`graphics.py`](http://mcsp.wartburg.edu/zelle/python/): for GUI rendering

---

## 🖼️ Output

- Sankey diagram visualization in a pop-up window
- Saved `.ps` and `.pdf` files in the working directory
- Includes diagram title, source label, and author credit

---

## 🔧 Future Improvements

- Error handling for malformed input files
- Support for multi-source or multi-stage diagrams
- Interactive features or zoom functionality
- Export to PNG or SVG formats

---

