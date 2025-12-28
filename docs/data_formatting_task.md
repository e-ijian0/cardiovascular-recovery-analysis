# Task: Format raw timestamp and blood pressure data

**Issue #2** (placeholder)

## Description
Before the new `calculate_recovery_slope` function can be used, the raw experimental data must be formatted correctly. This task involves preparing the timestamp and blood pressure data files to match the expected input format.

## Required formatting steps
1. **Convert timestamps to minutes from the end of the stressor task.**  
   - Raw timestamps may be recorded as absolute times (e.g., HH:MM:SS) or seconds relative to the start of the experiment.  
   - Subtract the time of the stressor offset to obtain minutes elapsed since the stressor ended.

2. **Ensure blood pressure readings are integers (or floats).**  
   - Remove any non‑numeric entries (e.g., “–”, “N/A”, “error”).  
   - If readings are stored as strings, convert them to numeric values.

3. **Align timestamps and blood pressure readings.**  
   - Each timestamp must correspond to exactly one systolic BP reading.  
   - Handle missing data appropriately (either interpolate or drop incomplete pairs).

4. **Export the cleaned data in a consistent structure.**  
   - A simple CSV with columns `time_min` and `systolic_bp` is sufficient.  
   - Alternatively, provide two lists (Python lists) that can be passed directly to `calculate_recovery_slope`.

## Dependencies
- This task must be completed before the recovery‑slope analysis can be run.
- The PR #1 (adding the slope function) is ready for review but cannot be merged until this formatting step is finished.

## Assignee
@e-ijian0