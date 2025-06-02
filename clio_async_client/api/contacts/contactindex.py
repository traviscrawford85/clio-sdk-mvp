from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_list import ContactList
from ...models.contactindex_custom_field_values import ContactindexCustomFieldValues
from ...models.contactindex_initial import ContactindexInitial
from ...models.contactindex_order import ContactindexOrder
from ...models.contactindex_type import ContactindexType
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client_only: Union[Unset, bool] = UNSET,
    clio_connect_only: Union[Unset, bool] = UNSET,
    created_since: Union[Unset, str] = UNSET,
    custom_field_ids: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, ContactindexCustomFieldValues] = UNSET,
    email_only: Union[Unset, bool] = UNSET,
    exclude_ids: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    initial: Union[Unset, ContactindexInitial] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, ContactindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    shared_resource_id: Union[Unset, int] = UNSET,
    type_: Union[Unset, ContactindexType] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["client_only"] = client_only

    params["clio_connect_only"] = clio_connect_only

    params["created_since"] = created_since

    params["custom_field_ids[]"] = custom_field_ids

    json_custom_field_values: Union[Unset, str] = UNSET
    if not isinstance(custom_field_values, Unset):
        json_custom_field_values = custom_field_values.value

    params["custom_field_values"] = json_custom_field_values

    params["email_only"] = email_only

    params["exclude_ids[]"] = exclude_ids

    params["fields"] = fields

    params["ids[]"] = ids

    json_initial: Union[Unset, str] = UNSET
    if not isinstance(initial, Unset):
        json_initial = initial.value

    params["initial"] = json_initial

    params["limit"] = limit

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    params["query"] = query

    params["shared_resource_id"] = shared_resource_id

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["updated_since"] = updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/contacts.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ContactList, Error]]:
    if response.status_code == 200:
        response_200 = ContactList.from_dict(response.json())

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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ContactList, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    client_only: Union[Unset, bool] = UNSET,
    clio_connect_only: Union[Unset, bool] = UNSET,
    created_since: Union[Unset, str] = UNSET,
    custom_field_ids: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, ContactindexCustomFieldValues] = UNSET,
    email_only: Union[Unset, bool] = UNSET,
    exclude_ids: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    initial: Union[Unset, ContactindexInitial] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, ContactindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    shared_resource_id: Union[Unset, int] = UNSET,
    type_: Union[Unset, ContactindexType] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[ContactList, Error]]:
    """Return the data for all Contacts

     Outlines the parameters, optional and required, used when requesting the data for all Contacts

    Args:
        client_only (Union[Unset, bool]):
        clio_connect_only (Union[Unset, bool]):
        created_since (Union[Unset, str]):
        custom_field_ids (Union[Unset, int]):
        custom_field_values (Union[Unset, ContactindexCustomFieldValues]):
        email_only (Union[Unset, bool]):
        exclude_ids (Union[Unset, int]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        initial (Union[Unset, ContactindexInitial]):
        limit (Union[Unset, int]):
        order (Union[Unset, ContactindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        shared_resource_id (Union[Unset, int]):
        type_ (Union[Unset, ContactindexType]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ContactList, Error]]
    """

    kwargs = _get_kwargs(
        client_only=client_only,
        clio_connect_only=clio_connect_only,
        created_since=created_since,
        custom_field_ids=custom_field_ids,
        custom_field_values=custom_field_values,
        email_only=email_only,
        exclude_ids=exclude_ids,
        fields=fields,
        ids=ids,
        initial=initial,
        limit=limit,
        order=order,
        page_token=page_token,
        query=query,
        shared_resource_id=shared_resource_id,
        type_=type_,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    client_only: Union[Unset, bool] = UNSET,
    clio_connect_only: Union[Unset, bool] = UNSET,
    created_since: Union[Unset, str] = UNSET,
    custom_field_ids: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, ContactindexCustomFieldValues] = UNSET,
    email_only: Union[Unset, bool] = UNSET,
    exclude_ids: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    initial: Union[Unset, ContactindexInitial] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, ContactindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    shared_resource_id: Union[Unset, int] = UNSET,
    type_: Union[Unset, ContactindexType] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[ContactList, Error]]:
    """Return the data for all Contacts

     Outlines the parameters, optional and required, used when requesting the data for all Contacts

    Args:
        client_only (Union[Unset, bool]):
        clio_connect_only (Union[Unset, bool]):
        created_since (Union[Unset, str]):
        custom_field_ids (Union[Unset, int]):
        custom_field_values (Union[Unset, ContactindexCustomFieldValues]):
        email_only (Union[Unset, bool]):
        exclude_ids (Union[Unset, int]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        initial (Union[Unset, ContactindexInitial]):
        limit (Union[Unset, int]):
        order (Union[Unset, ContactindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        shared_resource_id (Union[Unset, int]):
        type_ (Union[Unset, ContactindexType]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ContactList, Error]
    """

    return sync_detailed(
        client=client,
        client_only=client_only,
        clio_connect_only=clio_connect_only,
        created_since=created_since,
        custom_field_ids=custom_field_ids,
        custom_field_values=custom_field_values,
        email_only=email_only,
        exclude_ids=exclude_ids,
        fields=fields,
        ids=ids,
        initial=initial,
        limit=limit,
        order=order,
        page_token=page_token,
        query=query,
        shared_resource_id=shared_resource_id,
        type_=type_,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    client_only: Union[Unset, bool] = UNSET,
    clio_connect_only: Union[Unset, bool] = UNSET,
    created_since: Union[Unset, str] = UNSET,
    custom_field_ids: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, ContactindexCustomFieldValues] = UNSET,
    email_only: Union[Unset, bool] = UNSET,
    exclude_ids: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    initial: Union[Unset, ContactindexInitial] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, ContactindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    shared_resource_id: Union[Unset, int] = UNSET,
    type_: Union[Unset, ContactindexType] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[ContactList, Error]]:
    """Return the data for all Contacts

     Outlines the parameters, optional and required, used when requesting the data for all Contacts

    Args:
        client_only (Union[Unset, bool]):
        clio_connect_only (Union[Unset, bool]):
        created_since (Union[Unset, str]):
        custom_field_ids (Union[Unset, int]):
        custom_field_values (Union[Unset, ContactindexCustomFieldValues]):
        email_only (Union[Unset, bool]):
        exclude_ids (Union[Unset, int]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        initial (Union[Unset, ContactindexInitial]):
        limit (Union[Unset, int]):
        order (Union[Unset, ContactindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        shared_resource_id (Union[Unset, int]):
        type_ (Union[Unset, ContactindexType]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ContactList, Error]]
    """

    kwargs = _get_kwargs(
        client_only=client_only,
        clio_connect_only=clio_connect_only,
        created_since=created_since,
        custom_field_ids=custom_field_ids,
        custom_field_values=custom_field_values,
        email_only=email_only,
        exclude_ids=exclude_ids,
        fields=fields,
        ids=ids,
        initial=initial,
        limit=limit,
        order=order,
        page_token=page_token,
        query=query,
        shared_resource_id=shared_resource_id,
        type_=type_,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    client_only: Union[Unset, bool] = UNSET,
    clio_connect_only: Union[Unset, bool] = UNSET,
    created_since: Union[Unset, str] = UNSET,
    custom_field_ids: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, ContactindexCustomFieldValues] = UNSET,
    email_only: Union[Unset, bool] = UNSET,
    exclude_ids: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    initial: Union[Unset, ContactindexInitial] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, ContactindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    shared_resource_id: Union[Unset, int] = UNSET,
    type_: Union[Unset, ContactindexType] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[ContactList, Error]]:
    """Return the data for all Contacts

     Outlines the parameters, optional and required, used when requesting the data for all Contacts

    Args:
        client_only (Union[Unset, bool]):
        clio_connect_only (Union[Unset, bool]):
        created_since (Union[Unset, str]):
        custom_field_ids (Union[Unset, int]):
        custom_field_values (Union[Unset, ContactindexCustomFieldValues]):
        email_only (Union[Unset, bool]):
        exclude_ids (Union[Unset, int]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        initial (Union[Unset, ContactindexInitial]):
        limit (Union[Unset, int]):
        order (Union[Unset, ContactindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        shared_resource_id (Union[Unset, int]):
        type_ (Union[Unset, ContactindexType]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ContactList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            client_only=client_only,
            clio_connect_only=clio_connect_only,
            created_since=created_since,
            custom_field_ids=custom_field_ids,
            custom_field_values=custom_field_values,
            email_only=email_only,
            exclude_ids=exclude_ids,
            fields=fields,
            ids=ids,
            initial=initial,
            limit=limit,
            order=order,
            page_token=page_token,
            query=query,
            shared_resource_id=shared_resource_id,
            type_=type_,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
