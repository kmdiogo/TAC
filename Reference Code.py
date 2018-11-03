# @api_view(['POST'])
# def open_session(request, pk):
#     student = get_student_or_404(pk)
#     open_serializer = OpenSessionSerializer(data=request.data)
#     if open_serializer.is_valid():
#         if Session.objects.filter(student=student, endTime__isnull=True):
#             return Response({'detail': 'An open session already exists for this student'}, status=status.HTTP_400_BAD_REQUEST)
#         open_serializer.validated_data['student'] = student
#         open_serializer.save()
#         return Response(open_serializer.data, status=status.HTTP_201_CREATED)
#     return Response(open_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['PUT'])
# def close_session(request, pk):
#     get_student_or_404(pk)
#     request.data['student'] = pk
#     if Session.objects.filter(student__schoolId__iexact=pk, endTime__isnull=True).exists():
#         closeSession = Session.objects.get(student__schoolId__iexact=pk, endTime__isnull=True)
#         close_serializer = CloseSessionSerializer(data=request.data)
#         if close_serializer.is_valid():
#             closeSession.rating = close_serializer.data['rating']
#             closeSession.comments = close_serializer.data['comments']
#             closeSession.endTime = timezone.now()
#             closeSession.save()
#             return Response(close_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(close_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     return Response({"detail": 'An open session does exist for the student'}, status=status.HTTP_400_BAD_REQUEST)