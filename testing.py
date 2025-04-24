from ezc3d import c3d
import pandas as pd
from IPython.display import display
import plotly.express as px

myc3d = c3d('c3d_files/Dynamic1.c3d')
analog_data = myc3d['data']['analogs']
analog_labels = myc3d['parameters']['ANALOG']['LABELS']['value']
analog_df = pd.DataFrame(data=analog_data[0, :, :], index=analog_labels)
full_df = analog_df.T
full_df.reset_index(inplace=True)
full_df.rename(columns={'index': 'Time'}, inplace=True)
display(full_df)

# Plot using Plotly Express
fig = px.line(full_df, x='Time', y=full_df.columns[1:], 
              title="Analog Data Plot", labels={"value": "Analog Values", "Time": "Time"})
fig.show()

# Filter columns ending with "Fx", "Fy", or "Fz"
filtered_columns = [col for col in full_df.columns if col.endswith(("Fx", "Fy", "Fz"))]

# Plot the filtered data
fig_filtered = px.line(full_df, x='Time', y=filtered_columns, 
                       title="Filtered Analog Data Plot (Fx, Fy, Fz)", 
                       labels={"value": "Analog Values", "Time": "Time"})
fig_filtered.show()