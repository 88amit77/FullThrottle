from django.db import models

class Members(models.Model):
    real_name = models.CharField(max_length=30)
    tz = models.CharField(max_length=50)

    def __str__(self):
        return self.real_name


class InOut(models.Model):
    member = models.ForeignKey(Members, on_delete=models.CASCADE, related_name='activity_periods', null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
# members: [
# {
# id: "W012A3CDE",
# real_name: "Egon Spengler",
# tz: "America/Los_Angeles",
# activity_periods: [
# {
# start_time: "Feb 1 2020  1:33PM",
# end_time: "Feb 1 2020 1:54PM"
# },
# {
# start_time: "Mar 1 2020  11:11AM",
# end_time: "Mar 1 2020 2:00PM"
# },
# {
# start_time: "Mar 16 2020  5:33PM",
# end_time: "Mar 16 2020 8:02PM"
# }
# ]
# },
# {
# id: "W07QCRPA4",
# real_name: "Glinda Southgood",
# tz: "Asia/Kolkata",
# activity_periods: [
# {
# start_time: "Feb 1 2020  1:33PM",
# end_time: "Feb 1 2020 1:54PM"
# },
# {
# start_time: "Mar 1 2020  11:11AM",
# end_time: "Mar 1 2020 2:00PM"
# },
# {
# start_time: "Mar 16 2020  5:33PM",
# end_time: "Mar 16 2020 8:02PM"
# }
# ]
# }