#include <stdint.h>
#include "stts22h.h"

void STTS22H_WhoAmI(uint8_t *pData){
  HAL_I2C_Mem_Read(&hi2c1, STTS22H_ADDRESS, STTS22H_WHOAMI_REG, I2C_MEMADD_SIZE_8BIT, pData, 1, 1000);
}

float STTS22H_GetTemp(){
  uint8_t temp[2];
  int16_t raw_temperature;
  float temperature;

  // set one shot mode
  HAL_I2C_Mem_Write(&hi2c1, STTS22H_ADDRESS, STTS22H_CTRL_REG, I2C_MEMADD_SIZE_8BIT, (uint8_t[]){0x01}, 1, 1000);

  HAL_Delay(1000);

  // read temperature
  HAL_I2C_Mem_Read(&hi2c1, STTS22H_ADDRESS, STTS22H_DATA_REG, I2C_MEMADD_SIZE_8BIT, temp, 2, 1000);

  raw_temperature = (int16_t)((temp[1] << 8) |  temp[0]);
  temperature = raw_temperature * 0.01f;

  return temperature;
}
