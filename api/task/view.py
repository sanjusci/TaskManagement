
__author__ = "Sanjeev Kumar"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019."

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError, transaction
from rest_framework.permissions import IsAuthenticated
from api.function import Function
from api.task.model import Task
from api.task.serializers import TaskSerializer, UpdateTaskSerializer


class TaskList(APIView):
    """
    Class TaskList
    This class is used to get task details and create tasks.

    """

    permission_classes = (IsAuthenticated,)

    def get(self, request, pid):
        """
        Function get
        This function is used to get task data.

        :param pid:
            A pid that contains project id.
        :param request:
            A request that contains request params.

        :return:
            Return task data if exists else return empty dict.

        __author__ = "Sanjeev Kumar"
        __email__ = "sanju.sci9@gmail.com"
        """
        try:
            query = {'pid': pid, 'is_deleted': False}
            tasks = Task.objects.filter(**query)
            serializer = TaskSerializer(instance=tasks, many=True)
            if serializer.data:
                return Response(Function().success_response(
                    serializer.data,
                    'Task data has been fetched successfully!!'),
                    status=status.HTTP_200_OK
                )
            else:
                return Response(Function().success_response(
                    [], 'No Task data Found!!'),
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(Function().error_response(
                str(e), 'Something went wrong!! Please try again!!'),
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, pid):
        """
        Function post
        This function is used to store task data.

        :param pid:
            A pid that contains project id params.
        :param request:
            A request that contains request params.

        :return:
            Return success message if task data saved successfully else
            return
            error message.

        __author__ = "Sanjeev Kumar"
        __email__ = "sanju.sci9@gmail.com"
        """
        try:
            request_data = request.data
            request_data['pid'] = pid
            request_data['created_by'] = request.user.id
            request_data['updated_by'] = request.user.id
            transaction.set_autocommit(False)
            serializer = TaskSerializer(data=request_data)
            if serializer.is_valid():
                try:
                    serializer.save()
                except IntegrityError:
                    transaction.rollback()
                    return Response(Function().error_response(
                        serializer.errors,
                        'ERROR: task data is not saved!!'),
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )
            else:
                return Response(Function().error_response(
                    serializer.errors,
                    'ERROR: task data is not saved!!'),
                    status=status.HTTP_400_BAD_REQUEST
                )
            transaction.commit()
            return Response(Function().success_response(
                [], 'task has been created successfully!!'),
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                Function().error_response(
                    [str(e)], 'task data is not saved. Please try again!!'),
                status=status.HTTP_400_BAD_REQUEST
            )


class TaskDetails(APIView):
    """
    Class TaskDetails
    This class is used to fetch, update and detele task record stack.
    """

    permission_classes = (IsAuthenticated,)

    def get_object(self, pid, pk):
        """
        Function get_object
        This function is used to fetch task data record.

        :param pid:
            A pid that contains project id.
        :param pk:
            A pk that contains primary key value of task record.

        :return:
            Return task data if exist else return error.

        __author__ = "Sanjeev Kumar"
        __email__ = "sanju.sci9@gmail.com"
        """
        try:
            query = {
                'id': pk,
                'pid': pid,
                'is_deleted': False,
                'is_active': True
            }
            return Task.objects.get(**query)
        except Task.DoesNotExist:
            return False

    def get(self, request, pid, tk):
        """
        Function get
        This function is used to fetch single record.

        :param request:
            A request that contains request query data.
        :param pid:
            A pid that contains project id.
        :param tk:
            A tk that contains primary key value.

        :param format:
            A format that contains None value.

        :return:
            Return list of task data if exists else return empty list.

        __author__ = "Sanjeev Kumar"
        __email__ = "sanju.sci9@gmail.com"
        """
        try:
            task = self.get_object(pid, tk)
            if not task:
                return Response(Function().error_response(
                    [], 'Task record does not exist!!'),
                    status=status.HTTP_204_NO_CONTENT
                )
            serializer = TaskSerializer(task)
            if len(serializer.data) > 0:
                return Response(Function().success_response(
                    serializer.data,
                    'Task data has been fetched successfully!!'),
                    status=status.HTTP_200_OK
                )
            else:
                return Response(Function().success_response(
                    [], 'No Task data Found!!'),
                    status=status.HTTP_200_OK
                )

        except Exception as e:
            return Response(Function().error_response(
                str(e), 'Something went wrong!! Please try again!!'),
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pid, tk):
        """
        Function put
        This function is used to update task record using task id.

        :param request:
            A request that contains request query data.
        :param tk:
            A tk that contains primary key value.
        :param pid:
            A pid that contains project id.

        :return:
            Return true if record updated successfully else return false.

        __author__ = "Sanjeev Kumar"
        __email__ = "sanju.sci9@gmail.com"
        """
        try:
            request_data = request.data
            request_data['updated_by'] = request.user.id
            transaction.set_autocommit(False)
            task = self.get_object(pid, tk)
            if not task:
                return Response(Function().error_response(
                    [], 'Task record does not exist!!'),
                    status=status.HTTP_204_NO_CONTENT
                )
            serializer = UpdateTaskSerializer(
                instance=task,
                data=request_data,
                partial=True
            )
            if serializer.is_valid():
                try:
                    serializer.save()
                except IntegrityError:
                    transaction.rollback()
                    return Response(Function().error_response(
                        serializer.errors,
                        'ERROR: Task data is not updated!!'),
                        status=status.HTTP_409_CONFLICT
                    )
            else:
                return Response(Function().error_response(
                    serializer.errors,
                    'ERROR: Task data is not updated!!'),
                    status=status.HTTP_409_CONFLICT
                )
            transaction.commit()
            return Response(Function().success_response(
                [], 'Task data has been updated successfully!!'),
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(Function().error_response(
                str(e), 'Something went wrong!! Please try again!!'),
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pid, tk):
        """
        Function delete
        This function is used to delete(soft) task details.


        :param request:
            A request that contains request query data.
        :param tk:
            A tk that contains primary key value.
        :param pid:
            A pid that contains project id.

        :return:
            Return true if record successful deleted else return error message.

        __author__ = "Sanjeev Kumar"
        __email__ = "sanju.sci9@gmail.com"

        """
        try:
            transaction.set_autocommit(False)
            task = self.get_object(pid, tk)
            if not task:
                return Response(Function().error_response(
                    [], 'Task record does not exist!!'),
                    status=status.HTTP_404_NOT_FOUND
                )
            task.is_active = False
            task.is_deleted = True
            task.updated_by_id = request.user.id
            task.save()
            transaction.commit()
            return Response(Function().success_response(
                [], 'Task has been deleted successfully!!'),
                status=status.HTTP_200_OK
            )
        except Exception as e:
            transaction.rollback()
            return Response(Function().error_response(
                [str(e.message)], 'Task is not deleted!!'),
                status=status.HTTP_400_BAD_REQUEST
            )