import unittest
from datetime import datetime

from booking_scheduler import BookingScheduler
from schedule import Schedule, Customer

CAPACITY_PER_HOUR = 10
UNDER_CAPACITY = 6

NOT_ON_THE_HOUR = datetime.strptime('2024/7/20 10:47', '%Y/%m/%d %H:%M')
ON_THE_HOUR = datetime.strptime('2024/7/20 11:00', '%Y/%m/%d %H:%M')
CUSTOMER = Customer('jwh', '0')


class BookingSchedulerTest(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.scheduler = BookingScheduler(CAPACITY_PER_HOUR)

    def test_예약은_정시에만_가능하다_정시가_아닌경우_예약불가(self):
        schedule = Schedule(NOT_ON_THE_HOUR, UNDER_CAPACITY, CUSTOMER)

        with self.assertRaises(ValueError):
            self.scheduler.add_schedule(schedule)

    def test_예약은_정시에만_가능하다_정시인_경우_예약가능(self):
        schedule = Schedule(ON_THE_HOUR, UNDER_CAPACITY, CUSTOMER)

        self.scheduler.add_schedule(schedule)

        self.assertTrue(self.scheduler.has_schedule(schedule))

    def test_시간대별_인원제한이_있다_같은_시간대에_Capacity_초과할_경우_예외발생(self):
        schedule = Schedule(ON_THE_HOUR, UNDER_CAPACITY, CUSTOMER)
        self.scheduler.add_schedule(schedule)
        expected = 'Number of people is over restaurant capacity per hour'

        with self.assertRaises(ValueError) as context:
            new_schedule = Schedule(ON_THE_HOUR, UNDER_CAPACITY, CUSTOMER)
            self.scheduler.add_schedule(new_schedule)

        self.assertEqual(expected, str(context.exception))

    def test_시간대별_인원제한이_있다_같은_시간대가_다르면_Capacity_차있어도_스케쥴_추가_성공(self):
        pass

    def test_예약완료시_SMS는_무조건_발송(self):
        pass

    def test_이메일이_없는_경우에는_이메일_미발송(self):
        pass

    def test_이메일이_있는_경우에는_이메일_발송(self):
        pass

    def test_현재날짜가_일요일인_경우_예약불가_예외처리(self):
        pass

    def test_현재날짜가_일요일이_아닌경우_예약가능(self):
        pass


if __name__ == '__main__':
    unittest.main()
