deviceTimeseries()
wayConfig = readFromResource(GATEWAY_CONFIG_FILE);
        JsonNode gatewayConfigUpdated = readFromResource(GATEWAY_CONFIG_UPDATED_FILE);

        TEST_SERIAL_NUMBER_1 
TEST_SERIAL_NUMBER_2 
TEST_LAST_ACTIVITY_1 
DEVICE_CROW_INFO_FILE

{"app":"device","timestamp":"2025-06-12T14:46:47.368+02:00","level":"INFO","class":"com.protectline.device.ws.web.controller.DeviceControllerV1","method":"postDevice","caller_file_name":"DeviceControllerV1.java","line":180,"thread":"main","message":"CONT_V1_POST_DEVICE Ajout d'un device 'null 123456'"}
{"app":"device","timestamp":"2025-06-12T14:46:47.373+02:00","level":"INFO","class":"com.protectline.device.ws.service.impl.RoleServiceImpl","method":"checkRolesForToken","caller_file_name":"RoleServiceImpl.java","line":66,"thread":"main","message":"SERV_ROLE_NORMAL API method 'POST /v1/devices' will be executed with normal user"}
{"app":"device","timestamp":"2025-06-12T14:46:47.443+02:00","level":"WARN","class":"com.protectline.device.ws.web.exceptionhandler.ExceptionHandlerAdvice","method":"handleExceptionWithCodeAndParam","caller_file_name":"ExceptionHandlerAdvice.java","line":374,"thread":"main","message":"EXCEPTION_ERROR_03 Bad parameter : Model not respect the predefinited list"}
{"app":"device","timestamp":"2025-06-12T14:46:47.452+02:00","level":"INFO","class":"com.protectline.device.ws.web.controller.DeviceControllerV1","method":"postDevice","caller_file_name":"DeviceControllerV1.java","line":180,"thread":"main","message":"CONT_V1_POST_DEVICE Ajout d'un device 'ORG-CAMERA-INT 123456'"}
{"app":"device","timestamp":"2025-06-12T14:46:47.458+02:00","level":"INFO","class":"com.protectline.device.ws.service.impl.RoleServiceImpl","method":"checkRolesForToken","caller_file_name":"RoleServiceImpl.java","line":66,"thread":"main","message":"SERV_ROLE_NORMAL API method 'POST /v1/devices' will be executed with normal user"}
{"app":"device","timestamp":"2025-06-12T14:46:47.531+02:00","level":"WARN","class":"com.protectline.device.ws.web.exceptionhandler.ExceptionHandlerAdvice","method":"handleExceptionWithCodeAndParam","caller_file_name":"ExceptionHandlerAdvice.java","line":374,"thread":"main","message":"EXCEPTION_ERROR_03 Bad parameter : AdditionnalInfos not respect  the predefined list"}
