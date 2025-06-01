from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bill_list import BillList
from ...models.billindex_custom_field_values import BillindexCustomFieldValues
from ...models.billindex_order import BillindexOrder
from ...models.billindex_state import BillindexState
from ...models.billindex_status import BillindexStatus
from ...models.billindex_type import BillindexType
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    custom_field_values: Unset | BillindexCustomFieldValues = UNSET,
    due_after: Unset | str = UNSET,
    due_at: Unset | str = UNSET,
    due_before: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    issued_after: Unset | str = UNSET,
    issued_before: Unset | str = UNSET,
    last_sent_end_date: Unset | str = UNSET,
    last_sent_start_date: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | BillindexOrder = UNSET,
    originating_attorney_id: Unset | int = UNSET,
    overdue_only: Unset | bool = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | int = UNSET,
    responsible_attorney_id: Unset | int = UNSET,
    state: Unset | BillindexState = UNSET,
    status: Unset | BillindexStatus = UNSET,
    type_: Unset | BillindexType = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["client_id"] = client_id

    params["created_since"] = created_since

    json_custom_field_values: Unset | str = UNSET
    if not isinstance(custom_field_values, Unset):
        json_custom_field_values = custom_field_values.value

    params["custom_field_values"] = json_custom_field_values

    params["due_after"] = due_after

    params["due_at"] = due_at

    params["due_before"] = due_before

    params["fields"] = fields

    params["ids[]"] = ids

    params["issued_after"] = issued_after

    params["issued_before"] = issued_before

    params["last_sent_end_date"] = last_sent_end_date

    params["last_sent_start_date"] = last_sent_start_date

    params["limit"] = limit

    params["matter_id"] = matter_id

    json_order: Unset | str = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["originating_attorney_id"] = originating_attorney_id

    params["overdue_only"] = overdue_only

    params["page_token"] = page_token

    params["query"] = query

    params["responsible_attorney_id"] = responsible_attorney_id

    json_state: Unset | str = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    json_status: Unset | str = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_type_: Unset | str = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["updated_since"] = updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/bills.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BillList | Error | None:
    if response.status_code == 200:
        response_200 = BillList.from_dict(response.json())

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
) -> Response[BillList | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    client_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    custom_field_values: Unset | BillindexCustomFieldValues = UNSET,
    due_after: Unset | str = UNSET,
    due_at: Unset | str = UNSET,
    due_before: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    issued_after: Unset | str = UNSET,
    issued_before: Unset | str = UNSET,
    last_sent_end_date: Unset | str = UNSET,
    last_sent_start_date: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | BillindexOrder = UNSET,
    originating_attorney_id: Unset | int = UNSET,
    overdue_only: Unset | bool = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | int = UNSET,
    responsible_attorney_id: Unset | int = UNSET,
    state: Unset | BillindexState = UNSET,
    status: Unset | BillindexStatus = UNSET,
    type_: Unset | BillindexType = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[BillList | Error]:
    """Return the data for all Bills

     Outlines the parameters, optional and required, used when requesting the data for all Bills

    Args:
        client_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        custom_field_values (Union[Unset, BillindexCustomFieldValues]):
        due_after (Union[Unset, str]):
        due_at (Union[Unset, str]):
        due_before (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        issued_after (Union[Unset, str]):
        issued_before (Union[Unset, str]):
        last_sent_end_date (Union[Unset, str]):
        last_sent_start_date (Union[Unset, str]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, BillindexOrder]):
        originating_attorney_id (Union[Unset, int]):
        overdue_only (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        query (Union[Unset, int]):
        responsible_attorney_id (Union[Unset, int]):
        state (Union[Unset, BillindexState]):
        status (Union[Unset, BillindexStatus]):
        type_ (Union[Unset, BillindexType]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BillList, Error]]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        created_since=created_since,
        custom_field_values=custom_field_values,
        due_after=due_after,
        due_at=due_at,
        due_before=due_before,
        fields=fields,
        ids=ids,
        issued_after=issued_after,
        issued_before=issued_before,
        last_sent_end_date=last_sent_end_date,
        last_sent_start_date=last_sent_start_date,
        limit=limit,
        matter_id=matter_id,
        order=order,
        originating_attorney_id=originating_attorney_id,
        overdue_only=overdue_only,
        page_token=page_token,
        query=query,
        responsible_attorney_id=responsible_attorney_id,
        state=state,
        status=status,
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
    client: AuthenticatedClient | Client,
    client_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    custom_field_values: Unset | BillindexCustomFieldValues = UNSET,
    due_after: Unset | str = UNSET,
    due_at: Unset | str = UNSET,
    due_before: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    issued_after: Unset | str = UNSET,
    issued_before: Unset | str = UNSET,
    last_sent_end_date: Unset | str = UNSET,
    last_sent_start_date: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | BillindexOrder = UNSET,
    originating_attorney_id: Unset | int = UNSET,
    overdue_only: Unset | bool = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | int = UNSET,
    responsible_attorney_id: Unset | int = UNSET,
    state: Unset | BillindexState = UNSET,
    status: Unset | BillindexStatus = UNSET,
    type_: Unset | BillindexType = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> BillList | Error | None:
    """Return the data for all Bills

     Outlines the parameters, optional and required, used when requesting the data for all Bills

    Args:
        client_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        custom_field_values (Union[Unset, BillindexCustomFieldValues]):
        due_after (Union[Unset, str]):
        due_at (Union[Unset, str]):
        due_before (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        issued_after (Union[Unset, str]):
        issued_before (Union[Unset, str]):
        last_sent_end_date (Union[Unset, str]):
        last_sent_start_date (Union[Unset, str]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, BillindexOrder]):
        originating_attorney_id (Union[Unset, int]):
        overdue_only (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        query (Union[Unset, int]):
        responsible_attorney_id (Union[Unset, int]):
        state (Union[Unset, BillindexState]):
        status (Union[Unset, BillindexStatus]):
        type_ (Union[Unset, BillindexType]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BillList, Error]
    """

    return sync_detailed(
        client=client,
        client_id=client_id,
        created_since=created_since,
        custom_field_values=custom_field_values,
        due_after=due_after,
        due_at=due_at,
        due_before=due_before,
        fields=fields,
        ids=ids,
        issued_after=issued_after,
        issued_before=issued_before,
        last_sent_end_date=last_sent_end_date,
        last_sent_start_date=last_sent_start_date,
        limit=limit,
        matter_id=matter_id,
        order=order,
        originating_attorney_id=originating_attorney_id,
        overdue_only=overdue_only,
        page_token=page_token,
        query=query,
        responsible_attorney_id=responsible_attorney_id,
        state=state,
        status=status,
        type_=type_,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    client_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    custom_field_values: Unset | BillindexCustomFieldValues = UNSET,
    due_after: Unset | str = UNSET,
    due_at: Unset | str = UNSET,
    due_before: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    issued_after: Unset | str = UNSET,
    issued_before: Unset | str = UNSET,
    last_sent_end_date: Unset | str = UNSET,
    last_sent_start_date: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | BillindexOrder = UNSET,
    originating_attorney_id: Unset | int = UNSET,
    overdue_only: Unset | bool = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | int = UNSET,
    responsible_attorney_id: Unset | int = UNSET,
    state: Unset | BillindexState = UNSET,
    status: Unset | BillindexStatus = UNSET,
    type_: Unset | BillindexType = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[BillList | Error]:
    """Return the data for all Bills

     Outlines the parameters, optional and required, used when requesting the data for all Bills

    Args:
        client_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        custom_field_values (Union[Unset, BillindexCustomFieldValues]):
        due_after (Union[Unset, str]):
        due_at (Union[Unset, str]):
        due_before (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        issued_after (Union[Unset, str]):
        issued_before (Union[Unset, str]):
        last_sent_end_date (Union[Unset, str]):
        last_sent_start_date (Union[Unset, str]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, BillindexOrder]):
        originating_attorney_id (Union[Unset, int]):
        overdue_only (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        query (Union[Unset, int]):
        responsible_attorney_id (Union[Unset, int]):
        state (Union[Unset, BillindexState]):
        status (Union[Unset, BillindexStatus]):
        type_ (Union[Unset, BillindexType]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BillList, Error]]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        created_since=created_since,
        custom_field_values=custom_field_values,
        due_after=due_after,
        due_at=due_at,
        due_before=due_before,
        fields=fields,
        ids=ids,
        issued_after=issued_after,
        issued_before=issued_before,
        last_sent_end_date=last_sent_end_date,
        last_sent_start_date=last_sent_start_date,
        limit=limit,
        matter_id=matter_id,
        order=order,
        originating_attorney_id=originating_attorney_id,
        overdue_only=overdue_only,
        page_token=page_token,
        query=query,
        responsible_attorney_id=responsible_attorney_id,
        state=state,
        status=status,
        type_=type_,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    client_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    custom_field_values: Unset | BillindexCustomFieldValues = UNSET,
    due_after: Unset | str = UNSET,
    due_at: Unset | str = UNSET,
    due_before: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    issued_after: Unset | str = UNSET,
    issued_before: Unset | str = UNSET,
    last_sent_end_date: Unset | str = UNSET,
    last_sent_start_date: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | BillindexOrder = UNSET,
    originating_attorney_id: Unset | int = UNSET,
    overdue_only: Unset | bool = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | int = UNSET,
    responsible_attorney_id: Unset | int = UNSET,
    state: Unset | BillindexState = UNSET,
    status: Unset | BillindexStatus = UNSET,
    type_: Unset | BillindexType = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> BillList | Error | None:
    """Return the data for all Bills

     Outlines the parameters, optional and required, used when requesting the data for all Bills

    Args:
        client_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        custom_field_values (Union[Unset, BillindexCustomFieldValues]):
        due_after (Union[Unset, str]):
        due_at (Union[Unset, str]):
        due_before (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        issued_after (Union[Unset, str]):
        issued_before (Union[Unset, str]):
        last_sent_end_date (Union[Unset, str]):
        last_sent_start_date (Union[Unset, str]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, BillindexOrder]):
        originating_attorney_id (Union[Unset, int]):
        overdue_only (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        query (Union[Unset, int]):
        responsible_attorney_id (Union[Unset, int]):
        state (Union[Unset, BillindexState]):
        status (Union[Unset, BillindexStatus]):
        type_ (Union[Unset, BillindexType]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BillList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            client_id=client_id,
            created_since=created_since,
            custom_field_values=custom_field_values,
            due_after=due_after,
            due_at=due_at,
            due_before=due_before,
            fields=fields,
            ids=ids,
            issued_after=issued_after,
            issued_before=issued_before,
            last_sent_end_date=last_sent_end_date,
            last_sent_start_date=last_sent_start_date,
            limit=limit,
            matter_id=matter_id,
            order=order,
            originating_attorney_id=originating_attorney_id,
            overdue_only=overdue_only,
            page_token=page_token,
            query=query,
            responsible_attorney_id=responsible_attorney_id,
            state=state,
            status=status,
            type_=type_,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
