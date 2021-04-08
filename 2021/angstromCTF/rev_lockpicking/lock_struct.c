#include <stdint.h>

struct lock_struct
{
  int32_t b1;
  int32_t b2;
  int32_t b3;
  int8_t show_lock_positions;
  int8_t put_star;
  int8_t ctrl0;
  int8_t ctrl1;
  int8_t ctrl2;
  int8_t ctrl3;
  int8_t ctrl4;
};

struct lock_struct foo;