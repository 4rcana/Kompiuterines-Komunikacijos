#ifndef INC_STTS22H_H_
#define INC_STTS22H_H_

#include "main.h"

extern I2C_HandleTypeDef hi2c1;

#define 	STTS22H_ADDRESS				0x70
#define 	STTS22H_WHOAMI_REG			0x01
#define 	STTS22H_CTRL_REG			0x04
#define 	STTS22H_STATUS_REG			0x05
#define 	STTS22H_DATA_REG			0x06
#define 	STTS22H_RESET_REG			0x0c

void 	STTS22H_WhoAmI(uint8_t *pData);
void 	STTS22H_Temp_ODR_Enable();
void	STTS22H_Temp_Get(uint8_t *pData);






#endif /* INC_STTS22H_H_ */
