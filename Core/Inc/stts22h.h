#ifndef INC_STTS22H_H_
#define INC_STTS22H_H_

#include "main.h"

extern I2C_HandleTypeDef hi2c1;

#define STTS22H_ADDRESS			0x70
#define STTS22H_WHOAMI_REG		0x01
#define STTS22H_CTRL_REG		0x04
#define STTS22H_STATUS_REG		0x05
#define STTS22H_DATA_REG		0x06

void 	STTS22H_WhoAmI(uint8_t *pData);
float	STTS22H_GetTemp();





#endif /* INC_STTS22H_H_ */
