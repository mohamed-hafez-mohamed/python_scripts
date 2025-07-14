/****************************************************************************
* Title                 :   DRIVER   
* Filename              :   DRIVER_interface.h
* Author                :   Mohamed Hafez
* Origin Date           :   10/07/2025
* Version               :   1.0.0
* Compiler              :   GCC
* Target                :   STM32F103
* Notes                 :   None
*
*****************************************************************************/

/*************** INTERFACE CHANGE LIST **************************************
*
*    Date    Version   Author          Description 
*  10/07/25   1.0.0   Mohamed Hafez   Interface Created.
*
*****************************************************************************/

/** @file  DRIVER_interface.h
 *  @brief This module is for iteracting with driver
 *  This is the header file for the interfaces of driver
 */

#ifndef DRIVER_INTERFACE_H_
#define DRIVER_INTERFACE_H_

/******************************************************************************
* Includes
*******************************************************************************/

/******************************************************************************
* Preprocessor Constants
*******************************************************************************/

/******************************************************************************
* Configuration Constants
*******************************************************************************/

/******************************************************************************
* Macros
*******************************************************************************/
	
/******************************************************************************
* Typedefs
*******************************************************************************/
/**
 * @enum
 * @name DriverChannelNumber_t
 * @brief This enum represents ports.
 */
typedef enum
{
   PORTA, /**< PORT A */
   PORTB, /**< PORT B */
   PORTC, /**< PORT C */
   PORTD, /**< PORT D */
	NUMBER_OF_DRIVER_CHANNELS
}DriverChannelNumber_t;
/******************************************************************************
* Variables
*******************************************************************************/

/******************************************************************************
* Function Prototypes
*******************************************************************************/
/**
 * @name   Init
 * @brief  Intialize module.
 * @param  Cpnfig_ptr pointer to configuration parameter.
 * @return Error code.
 */
Std_Return Init(Config_t* Config_ptr);

/**
 * @brief  Main function.
 * @param  void.
 * @return void.
 */
void MainFunction(void);

/**
 * @brief  Get variable.
 * @param  Data_ptr pointer to data.
 * @return Error code.
 */
Std_Return Get(uint8* Data_ptr);

/**
 * @brief  Set variable.
 * @param  Data data.
 * @return Error code.
 */
Std_Return Set(uint8 Data);

#endif /*File_H_*/

/*** End of File **************************************************************/