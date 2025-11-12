#include <stdint.h>
#include "stts22h.h"

void STTS22H_WhoAmI(uint8_t *pData){
  HAL_I2C_Mem_Read(&hi2c1, STTS22H_ADDRESS, STTS22H_WHOAMI_REG, I2C_MEMADD_SIZE_8BIT, pData, 1, 1000);
}

void STTS22H_Temp_ODR_Enable(){
	HAL_I2C_Mem_Write(&hi2c1, STTS22H_ADDRESS, STTS22H_RESET_REG, I2C_MEMADD_SIZE_8BIT, (uint8_t[]){0x02}, 1, 100);

	HAL_I2C_Mem_Write(&hi2c1, STTS22H_ADDRESS, STTS22H_RESET_REG, I2C_MEMADD_SIZE_8BIT, (uint8_t[]){0x00}, 1, 100);

	HAL_I2C_Mem_Write(&hi2c1, STTS22H_ADDRESS, STTS22H_CTRL_REG, I2C_MEMADD_SIZE_8BIT, (uint8_t[]){0x2c}, 1, 100);

	HAL_Delay(12);
}

void STTS22H_Temp_Get(uint8_t *pData){
  HAL_I2C_Mem_Read(&hi2c1, STTS22H_ADDRESS, STTS22H_DATA_REG, I2C_MEMADD_SIZE_8BIT, pData, 2, 100);
}
