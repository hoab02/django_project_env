# views.py
from rest_framework import generics
from .models import Robot
from .serializers import RobotSerializer
from .utils import generate_random_position_id

# View để trả về danh sách các robots
class RobotListView(generics.ListAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer

# View để tạo mới một robot
class RobotCreateView(generics.CreateAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer

class RobotDetailView(generics.RetrieveAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    lookup_field = 'robot_id'  # Sử dụng robot_id làm khóa chính

    def get(self, request, *args, **kwargs):
        # Truy cập robot
        response = super().get(request, *args, **kwargs)
        robot = self.get_object()

        # Sinh ngẫu nhiên position_id và cập nhật robot
        new_position_id = generate_random_position_id()
        robot.position_id = new_position_id
        robot.save()

        # Trả về thông tin robot đã được cập nhật
        response.data['position_id'] = new_position_id
        return response
