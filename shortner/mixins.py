# -*- coding: utf-8 -*-

from typing import Optional, Union

from rest_framework.response import Response

__all__ = ["DefaultResponseMixin", "formatted_response_dict"]


def formatted_response_dict(
    status: int = 200, msg: str = "OK", data: Optional[Union[dict, list]] = {},
) -> dict:

    return {
        "status": status,
        "msg": msg,
        "data": data,
    }


class DefaultResponseMixin:
    """
    Provides a default response format that should be used by all views.

        {
            status: <integer:code>,
            msg: <string>,
            data: <obj>
        }
    """

    STATUS_MSGS = {
        200: "OK",
        201: "CREATED",
        204: "NO CONTENT",
        403: "FORBIDDEN",
        400: "BAD REQUEST",
        404: "NOT FOUND",
        501: "NOT IMPLEMENTED",
    }

    csrf_exempt = True

    def create_response(
        self, status: int = 200, msg: str = "", data: dict = None
    ) -> Response:
        data = self.create_response_data(status, msg, data)
        return Response(status=status, data=data)

    def create_response_data(
        self, status: int = 200, msg: str = "", data: dict = None
    ) -> dict:
        msg = msg or self.STATUS_MSGS.get(status, "")
        return formatted_response_dict(status=status, msg=msg, data=data)

    def default_200(self) -> Response:
        """
        Returns an empty '200 OK' response
        """
        return self.create_response()


