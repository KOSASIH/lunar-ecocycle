# API Reference for the Lunar EcoCycle Project

## Overview
This document provides details about the API endpoints available in the Lunar EcoCycle system.

## Base URL
http://localhost:5000/api


## Endpoints

### 1. Waste Sorting API
- **Endpoint**: `/api/waste-sort`
- **Method**: `POST`
- **Description**: Sorts the given waste type.
- **Request Body**:

 ```json
 1. {
 2.   "waste_type": "plastic"
 3. }
 ```

 - Response:

  ```json
 1. {
 2. "status": "success",
 3. "sorted_type": "sorted_plastic"
 4. }
```

### ISRU Module API

- Endpoint: /api/extract-resource
- Method: POST
- Description: Extracts a specified resource.
- Request Body:

```json
1. {
2.  "resource": "water"
3. }
```

- Response:

```json
1. {
2.  "status": "success",
3.  "extracted": true
4. }
```

# 3. Bioregenerative System API

- Endpoint: /api/grow-plant
- Method: POST
- Description: Initiates the growth of a specified plant.
- Request Body:

```json
1. {
2.  "plant_type": "tomato"
3. }
```

- **Response**:

```json
1. {
2.  "status": "success",
3.  "growth_status": "growing"
4. }
```

# 4. 3D Printing Module API

- Endpoint: /api/print-object
- Method: POST
- Description: Prints a specified object.
- Request Body:

```json
1. {
2.  "object_type": "component"
3. }
```

- Response:

```json
1. {
2.  "status": "success",
3.  "printed": true
4. }
```

# 5. Robotics System API

- Endpoint: /api/execute-task
- Method: POST
- Description: Executes a specified task.
- Request Body:

```json
1. {
2.  "task": "maintenance"
3. }
```

- Response:

```json
1. {
2.  "status": "success",
3.  "task_status": "completed"
4. }
```

# 6. Energy Management System API

- Endpoint: /api/distribute-energy
- Method: POST
- Description: Distributes energy to specified components.
- Request Body:

```json
1. {
2.  "components": ["Waste Sorting Module", "ISRU Module"]
3. }
```

- Response:

```json
1. {
2.  "status": "success",
3.  "energy_distributed": true
4. }
