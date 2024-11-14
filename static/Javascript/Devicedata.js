function validateForm() {
    const deviceId = document.getElementById('device_id').value.trim();
    const batteryLevel = parseFloat(document.getElementById('battery_level').value.trim());
    const sensorTemp = document.getElementById('sensor_temp').value.trim();
    const routeFrom = document.getElementById('route_from').value.trim();
    const routeTo = document.getElementById('route_to').value.trim();

    // Validate each field
    if (!deviceId || !batteryLevel || !sensorTemp || !routeFrom || !routeTo) {
        document.getElementById('error_message').textContent = 'All fields are required.';
        return false;
    }

    if (batteryLevel < 0 || batteryLevel > 100) {
        document.getElementById('error_message').textContent = 'Battery Level must be between 0 and 100.';
        return false;
    }

    if (isNaN(sensorTemp)) {
        document.getElementById('error_message').textContent = 'First Sensor Temperature must be a number.';
        return false;
    }

    // If all validations pass
    alert('Form submitted successfully!');
    return true;
}
