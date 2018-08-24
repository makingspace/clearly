# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import clearly_pb2 as protos_dot_clearly__pb2


class ClearlyServerStub(object):
  """
  Server objects.

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.capture_realtime = channel.unary_stream(
        '/ClearlyServer/capture_realtime',
        request_serializer=protos_dot_clearly__pb2.CaptureRequest.SerializeToString,
        response_deserializer=protos_dot_clearly__pb2.RealtimeEventMessage.FromString,
        )
    self.filter_tasks = channel.unary_stream(
        '/ClearlyServer/filter_tasks',
        request_serializer=protos_dot_clearly__pb2.FilterTasksRequest.SerializeToString,
        response_deserializer=protos_dot_clearly__pb2.TaskMessage.FromString,
        )
    self.filter_workers = channel.unary_stream(
        '/ClearlyServer/filter_workers',
        request_serializer=protos_dot_clearly__pb2.FilterWorkersRequest.SerializeToString,
        response_deserializer=protos_dot_clearly__pb2.WorkerMessage.FromString,
        )
    self.find_task = channel.unary_unary(
        '/ClearlyServer/find_task',
        request_serializer=protos_dot_clearly__pb2.FindTaskRequest.SerializeToString,
        response_deserializer=protos_dot_clearly__pb2.TaskMessage.FromString,
        )
    self.seen_tasks = channel.unary_unary(
        '/ClearlyServer/seen_tasks',
        request_serializer=protos_dot_clearly__pb2.Empty.SerializeToString,
        response_deserializer=protos_dot_clearly__pb2.SeenTasksMessage.FromString,
        )
    self.reset_tasks = channel.unary_unary(
        '/ClearlyServer/reset_tasks',
        request_serializer=protos_dot_clearly__pb2.Empty.SerializeToString,
        response_deserializer=protos_dot_clearly__pb2.Empty.FromString,
        )
    self.get_stats = channel.unary_unary(
        '/ClearlyServer/get_stats',
        request_serializer=protos_dot_clearly__pb2.Empty.SerializeToString,
        response_deserializer=protos_dot_clearly__pb2.StatsMessage.FromString,
        )


class ClearlyServerServicer(object):
  """
  Server objects.

  """

  def capture_realtime(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def filter_tasks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def filter_workers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def find_task(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def seen_tasks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def reset_tasks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def get_stats(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ClearlyServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'capture_realtime': grpc.unary_stream_rpc_method_handler(
          servicer.capture_realtime,
          request_deserializer=protos_dot_clearly__pb2.CaptureRequest.FromString,
          response_serializer=protos_dot_clearly__pb2.RealtimeEventMessage.SerializeToString,
      ),
      'filter_tasks': grpc.unary_stream_rpc_method_handler(
          servicer.filter_tasks,
          request_deserializer=protos_dot_clearly__pb2.FilterTasksRequest.FromString,
          response_serializer=protos_dot_clearly__pb2.TaskMessage.SerializeToString,
      ),
      'filter_workers': grpc.unary_stream_rpc_method_handler(
          servicer.filter_workers,
          request_deserializer=protos_dot_clearly__pb2.FilterWorkersRequest.FromString,
          response_serializer=protos_dot_clearly__pb2.WorkerMessage.SerializeToString,
      ),
      'find_task': grpc.unary_unary_rpc_method_handler(
          servicer.find_task,
          request_deserializer=protos_dot_clearly__pb2.FindTaskRequest.FromString,
          response_serializer=protos_dot_clearly__pb2.TaskMessage.SerializeToString,
      ),
      'seen_tasks': grpc.unary_unary_rpc_method_handler(
          servicer.seen_tasks,
          request_deserializer=protos_dot_clearly__pb2.Empty.FromString,
          response_serializer=protos_dot_clearly__pb2.SeenTasksMessage.SerializeToString,
      ),
      'reset_tasks': grpc.unary_unary_rpc_method_handler(
          servicer.reset_tasks,
          request_deserializer=protos_dot_clearly__pb2.Empty.FromString,
          response_serializer=protos_dot_clearly__pb2.Empty.SerializeToString,
      ),
      'get_stats': grpc.unary_unary_rpc_method_handler(
          servicer.get_stats,
          request_deserializer=protos_dot_clearly__pb2.Empty.FromString,
          response_serializer=protos_dot_clearly__pb2.StatsMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ClearlyServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
