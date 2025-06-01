from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_list import CustomFieldList
from ...models.custom_fieldindex_field_type import CustomFieldindexFieldType
from ...models.custom_fieldindex_order import CustomFieldindexOrder
from ...models.custom_fieldindex_parent_type import CustomFieldindexParentType
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created_since: Unset | str = UNSET,
    deleted: Unset | bool = UNSET,
    field_type: Unset | CustomFieldindexFieldType = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    order: Unset | CustomFieldindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    parent_type: Unset | CustomFieldindexParentType = UNSET,
    query: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    visible_and_required: Unset | bool = UNSET,
    x_api_version: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["created_since"] = created_since

    params["deleted"] = deleted

    json_field_type: Unset | str = UNSET
    if not isinstance(field_type, Unset):
        json_field_type = field_type.value

    params["field_type"] = json_field_type

    params["fields"] = fields

    params["ids[]"] = ids

    params["limit"] = limit

    json_order: Unset | str = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    json_parent_type: Unset | str = UNSET
    if not isinstance(parent_type, Unset):
        json_parent_type = parent_type.value

    params["parent_type"] = json_parent_type

    params["query"] = query

    params["updated_since"] = updated_since

    params["visible_and_required"] = visible_and_required

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/custom_fields.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomFieldList | Error | None:
    if response.status_code == 200:
        response_200 = CustomFieldList.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CustomFieldList | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    created_since: Unset | str = UNSET,
    deleted: Unset | bool = UNSET,
    field_type: Unset | CustomFieldindexFieldType = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    order: Unset | CustomFieldindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    parent_type: Unset | CustomFieldindexParentType = UNSET,
    query: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    visible_and_required: Unset | bool = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[CustomFieldList | Error]:
    """Return the data for all CustomFields

     Outlines the parameters, optional and required, used when requesting the data for all CustomFields

    Args:
        created_since (Union[Unset, str]):
        deleted (Union[Unset, bool]):
        field_type (Union[Unset, CustomFieldindexFieldType]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, CustomFieldindexOrder]):
        page_token (Union[Unset, str]):
        parent_type (Union[Unset, CustomFieldindexParentType]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        visible_and_required (Union[Unset, bool]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomFieldList, Error]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        deleted=deleted,
        field_type=field_type,
        fields=fields,
        ids=ids,
        limit=limit,
        order=order,
        page_token=page_token,
        parent_type=parent_type,
        query=query,
        updated_since=updated_since,
        visible_and_required=visible_and_required,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    created_since: Unset | str = UNSET,
    deleted: Unset | bool = UNSET,
    field_type: Unset | CustomFieldindexFieldType = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    order: Unset | CustomFieldindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    parent_type: Unset | CustomFieldindexParentType = UNSET,
    query: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    visible_and_required: Unset | bool = UNSET,
    x_api_version: Unset | str = UNSET,
) -> CustomFieldList | Error | None:
    """Return the data for all CustomFields

     Outlines the parameters, optional and required, used when requesting the data for all CustomFields

    Args:
        created_since (Union[Unset, str]):
        deleted (Union[Unset, bool]):
        field_type (Union[Unset, CustomFieldindexFieldType]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, CustomFieldindexOrder]):
        page_token (Union[Unset, str]):
        parent_type (Union[Unset, CustomFieldindexParentType]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        visible_and_required (Union[Unset, bool]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomFieldList, Error]
    """

    return sync_detailed(
        client=client,
        created_since=created_since,
        deleted=deleted,
        field_type=field_type,
        fields=fields,
        ids=ids,
        limit=limit,
        order=order,
        page_token=page_token,
        parent_type=parent_type,
        query=query,
        updated_since=updated_since,
        visible_and_required=visible_and_required,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    created_since: Unset | str = UNSET,
    deleted: Unset | bool = UNSET,
    field_type: Unset | CustomFieldindexFieldType = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    order: Unset | CustomFieldindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    parent_type: Unset | CustomFieldindexParentType = UNSET,
    query: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    visible_and_required: Unset | bool = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[CustomFieldList | Error]:
    """Return the data for all CustomFields

     Outlines the parameters, optional and required, used when requesting the data for all CustomFields

    Args:
        created_since (Union[Unset, str]):
        deleted (Union[Unset, bool]):
        field_type (Union[Unset, CustomFieldindexFieldType]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, CustomFieldindexOrder]):
        page_token (Union[Unset, str]):
        parent_type (Union[Unset, CustomFieldindexParentType]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        visible_and_required (Union[Unset, bool]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomFieldList, Error]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        deleted=deleted,
        field_type=field_type,
        fields=fields,
        ids=ids,
        limit=limit,
        order=order,
        page_token=page_token,
        parent_type=parent_type,
        query=query,
        updated_since=updated_since,
        visible_and_required=visible_and_required,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    created_since: Unset | str = UNSET,
    deleted: Unset | bool = UNSET,
    field_type: Unset | CustomFieldindexFieldType = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    order: Unset | CustomFieldindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    parent_type: Unset | CustomFieldindexParentType = UNSET,
    query: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    visible_and_required: Unset | bool = UNSET,
    x_api_version: Unset | str = UNSET,
) -> CustomFieldList | Error | None:
    """Return the data for all CustomFields

     Outlines the parameters, optional and required, used when requesting the data for all CustomFields

    Args:
        created_since (Union[Unset, str]):
        deleted (Union[Unset, bool]):
        field_type (Union[Unset, CustomFieldindexFieldType]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, CustomFieldindexOrder]):
        page_token (Union[Unset, str]):
        parent_type (Union[Unset, CustomFieldindexParentType]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        visible_and_required (Union[Unset, bool]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomFieldList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            created_since=created_since,
            deleted=deleted,
            field_type=field_type,
            fields=fields,
            ids=ids,
            limit=limit,
            order=order,
            page_token=page_token,
            parent_type=parent_type,
            query=query,
            updated_since=updated_since,
            visible_and_required=visible_and_required,
            x_api_version=x_api_version,
        )
    ).parsed
