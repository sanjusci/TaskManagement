
__author__ = "Sanjeev Kumar"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019."

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError, transaction
from rest_framework.permissions import IsAuthenticated
from api.function import Function
from api.project.model import Project
from api.project.serializers import ProjectSerializer, UpdateProjectSerializer


class ProjectList(APIView):
    """
    Class ProjectList
    This class is used to get project details and create projects.

    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        Function get
        This function is used to get project data.

        :param request:
            A request that contains request params.

        :return:
            Return project data if exists else return empty dict.

        __author__ = "Sanjeev Kumar"
        __email__ = "sanju.sci9@gmail.com"
        """
        try:
            query = {'is_deleted': False}
            projects = Project.objects.filter(**query)
            serializer = ProjectSerializer(instance=projects, many=True)
            if serializer.data:
                return Response(Function().success_response(
                    serializer.data,
                    'Project data has been fetched successfully!!'),
                    status=status.HTTP_200_OK
                )
            else:
                return Response(Function().success_response(
                    [], 'No Project data Found!!'),
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(Function().error_response(
                str(e), 'Something went wrong!! Please try again!!'),
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        """
        Function post
        This function is used to store project data.

        :param request:
            A request that contains request params.

        :return:
            Return success message if project data saved successfully else
            return
            error message.

        __author__ = "Sanjeev Kumar"
        __email__ = "sanju.sci9@gmail.com"
        """
        try:
            request_data = request.data
            request_data['created_by'] = request.user.id
            request_data['updated_by'] = request.user.id
            transaction.set_autocommit(False)
            serializer = ProjectSerializer(data=request_data)
            if serializer.is_valid():
                try:
                    serializer.save()
                except IntegrityError:
                    transaction.rollback()
                    return Response(Function().error_response(
                        serializer.errors,
                        'ERROR: project data is not saved!!'),
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )
            else:
                return Response(Function().error_response(
                    serializer.errors,
                    'ERROR: project data is not saved!!'),
                    status=status.HTTP_400_BAD_REQUEST
                )
            transaction.commit()
            return Response(Function().success_response(
                [], 'project has been created successfully!!'),
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                Function().error_response(
                    [str(e)], 'project data is not saved. Please try again!!'),
                status=status.HTTP_400_BAD_REQUEST
            )


class ProjectDetails(APIView):
    """
    Class ProjectDetails
    This class is used to fetch, update and detele project record stack.
    """

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        """
        Function get_object
        This function is used to fetch project data record.

        :param pk:
            A pk that contains primary key value of project record.

        :return:
            Return project data if exist else return error.

        __author__ = "Sanjeev Kumar"
        __email__ = "sanju.sci9@gmail.com"
        """
        try:
            query = {'id': pk, 'is_deleted': False, 'is_active': True}
            return Project.objects.get(**query)
        except Project.DoesNotExist:
            return False

    def get(self, request, pk):
        """
        Function get
        This function is used to fetch single record.

        :param request:
            A request that contains request query data.
        :param pk:
            A pk that contains primary key value.

        :param format:
            A format that contains None value.

        :return:
            Return list of project data if exists else return empty list.

        __author__ = "Sanjeev Kumar"
        __email__ = "sanju.sci9@gmail.com"
        """
        try:
            project = self.get_object(pk)
            if not project:
                return Response(Function().error_response(
                    [], 'Project record does not exist!!'),
                    status=status.HTTP_204_NO_CONTENT
                )
            serializer = ProjectSerializer(project)
            if len(serializer.data) > 0:
                return Response(Function().success_response(
                    serializer.data,
                    'Project data has been fetched successfully!!'),
                    status=status.HTTP_200_OK
                )
            else:
                return Response(Function().success_response(
                    [], 'No Project data Found!!'),
                    status=status.HTTP_200_OK
                )

        except Exception as e:
            return Response(Function().error_response(
                str(e), 'Something went wrong!! Please try again!!'),
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk):
        """
        Function put
        This function is used to update project record using project id.

        :param request:
            A request that contains request query data.
        :param pk:
            A pk that contains primary key value.
        :param format:
            A format that contains None value.

        :return:
            Return true if record updated successfully else return false.

        __author__ = "Sanjeev Kumar"
        __email__ = "sanju.sci9@gmail.com"
        """
        try:
            request_data = request.data
            request_data['updated_by'] = request.user.id
            transaction.set_autocommit(False)
            project = self.get_object(pk)
            if not project:
                return Response(Function().error_response(
                    [], 'Project record does not exist!!'),
                    status=status.HTTP_204_NO_CONTENT
                )
            serializer = UpdateProjectSerializer(
                instance=project,
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
                        'ERROR: Project data is not updated!!'),
                        status=status.HTTP_409_CONFLICT
                    )
            else:
                return Response(Function().error_response(
                    serializer.errors,
                    'ERROR: Project data is not updated!!'),
                    status=status.HTTP_409_CONFLICT
                )
            transaction.commit()
            return Response(Function().success_response(
                [], 'Project data has been updated successfully!!'),
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(Function().error_response(
                str(e), 'Something went wrong!! Please try again!!'),
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk):
        """
        Function delete
        This function is used to delete(soft) project details.

        :param request:
            A request that contains request query data.
        :param pk:
            A pk that contains primary key value.
        :param format:
            A format that contains None value.

        :return:
            Return true if record successful deleted else return error message.

        __author__ = "Sanjeev Kumar"
        __email__ = "sanju.sci9@gmail.com"

        """
        try:
            transaction.set_autocommit(False)
            project = self.get_object(pk)
            if not project:
                return Response(Function().error_response(
                    [], 'Project record does not exist!!'),
                    status=status.HTTP_404_NOT_FOUND
                )
            project.is_active = False
            project.is_deleted = True
            project.updated_by_id = request.user.id
            project.save()
            transaction.commit()
            return Response(Function().success_response(
                [], 'Project has been deleted successfully!!'),
                status=status.HTTP_200_OK
            )
        except Exception as e:
            transaction.rollback()
            return Response(Function().error_response(
                [str(e.message)], 'Project is not deleted!!'),
                status=status.HTTP_400_BAD_REQUEST
            )