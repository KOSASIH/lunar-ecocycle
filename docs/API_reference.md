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

  ```
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

```
1. {
2.  "resource": "water"
3. }
```

- Response:

```
1. {
2.  "status": "success",
3.  "extracted": true
4. }
```
