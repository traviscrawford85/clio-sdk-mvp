from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_list import ActivityList
from ...models.activityindex_order import ActivityindexOrder
from ...models.activityindex_status import ActivityindexStatus
from ...models.activityindex_type import ActivityindexType
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    activity_description_id: Unset | int = UNSET,
    calendar_entry_id: Unset | int = UNSET,
    communication_id: Unset | int = UNSET,
    contact_note_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    end_date: Unset | str = UNSET,
    expense_category_id: Unset | int = UNSET,
    fields: Unset | str = UNSET,
    flat_rate: Unset | bool = UNSET,
    grant_transaction_id: Unset | int = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    matter_note_id: Unset | int = UNSET,
    only_unaccounted_for: Unset | bool = UNSET,
    order: Unset | ActivityindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    start_date: Unset | str = UNSET,
    status: Unset | ActivityindexStatus = UNSET,
    task_id: Unset | int = UNSET,
    type_: Unset | ActivityindexType = UNSET,
    updated_since: Unset | str = UNSET,
    user_id: Unset | int = UNSET,
    x_api_version: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["activity_description_id"] = activity_description_id

    params["calendar_entry_id"] = calendar_entry_id

    params["communication_id"] = communication_id

    params["contact_note_id"] = contact_note_id

    params["created_since"] = created_since

    params["end_date"] = end_date

    params["expense_category_id"] = expense_category_id

    params["fields"] = fields

    params["flat_rate"] = flat_rate

    params["grant_transaction_id"] = grant_transaction_id

    params["ids[]"] = ids

    params["limit"] = limit

    params["matter_id"] = matter_id

    params["matter_note_id"] = matter_note_id

    params["only_unaccounted_for"] = only_unaccounted_for

    json_order: Unset | str = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    params["query"] = query

    params["start_date"] = start_date

    json_status: Unset | str = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["task_id"] = task_id

    json_type_: Unset | str = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["updated_since"] = updated_since

    params["user_id"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/activities.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivityList | Error | None:
    if response.status_code == 200:
        response_200 = ActivityList.from_dict(response.json())

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
) -> Response[ActivityList | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    activity_description_id: Unset | int = UNSET,
    calendar_entry_id: Unset | int = UNSET,
    communication_id: Unset | int = UNSET,
    contact_note_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    end_date: Unset | str = UNSET,
    expense_category_id: Unset | int = UNSET,
    fields: Unset | str = UNSET,
    flat_rate: Unset | bool = UNSET,
    grant_transaction_id: Unset | int = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    matter_note_id: Unset | int = UNSET,
    only_unaccounted_for: Unset | bool = UNSET,
    order: Unset | ActivityindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    start_date: Unset | str = UNSET,
    status: Unset | ActivityindexStatus = UNSET,
    task_id: Unset | int = UNSET,
    type_: Unset | ActivityindexType = UNSET,
    updated_since: Unset | str = UNSET,
    user_id: Unset | int = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[ActivityList | Error]:
    """Return the data for all Activities

     Outlines the parameters, optional and required, used when requesting the data for all Activities

    Args:
        activity_description_id (Union[Unset, int]):
        calendar_entry_id (Union[Unset, int]):
        communication_id (Union[Unset, int]):
        contact_note_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        end_date (Union[Unset, str]):
        expense_category_id (Union[Unset, int]):
        fields (Union[Unset, str]):
        flat_rate (Union[Unset, bool]):
        grant_transaction_id (Union[Unset, int]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        matter_note_id (Union[Unset, int]):
        only_unaccounted_for (Union[Unset, bool]):
        order (Union[Unset, ActivityindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        start_date (Union[Unset, str]):
        status (Union[Unset, ActivityindexStatus]):
        task_id (Union[Unset, int]):
        type_ (Union[Unset, ActivityindexType]):
        updated_since (Union[Unset, str]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActivityList, Error]]
    """

    kwargs = _get_kwargs(
        activity_description_id=activity_description_id,
        calendar_entry_id=calendar_entry_id,
        communication_id=communication_id,
        contact_note_id=contact_note_id,
        created_since=created_since,
        end_date=end_date,
        expense_category_id=expense_category_id,
        fields=fields,
        flat_rate=flat_rate,
        grant_transaction_id=grant_transaction_id,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        matter_note_id=matter_note_id,
        only_unaccounted_for=only_unaccounted_for,
        order=order,
        page_token=page_token,
        query=query,
        start_date=start_date,
        status=status,
        task_id=task_id,
        type_=type_,
        updated_since=updated_since,
        user_id=user_id,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    activity_description_id: Unset | int = UNSET,
    calendar_entry_id: Unset | int = UNSET,
    communication_id: Unset | int = UNSET,
    contact_note_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    end_date: Unset | str = UNSET,
    expense_category_id: Unset | int = UNSET,
    fields: Unset | str = UNSET,
    flat_rate: Unset | bool = UNSET,
    grant_transaction_id: Unset | int = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    matter_note_id: Unset | int = UNSET,
    only_unaccounted_for: Unset | bool = UNSET,
    order: Unset | ActivityindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    start_date: Unset | str = UNSET,
    status: Unset | ActivityindexStatus = UNSET,
    task_id: Unset | int = UNSET,
    type_: Unset | ActivityindexType = UNSET,
    updated_since: Unset | str = UNSET,
    user_id: Unset | int = UNSET,
    x_api_version: Unset | str = UNSET,
) -> ActivityList | Error | None:
    """Return the data for all Activities

     Outlines the parameters, optional and required, used when requesting the data for all Activities

    Args:
        activity_description_id (Union[Unset, int]):
        calendar_entry_id (Union[Unset, int]):
        communication_id (Union[Unset, int]):
        contact_note_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        end_date (Union[Unset, str]):
        expense_category_id (Union[Unset, int]):
        fields (Union[Unset, str]):
        flat_rate (Union[Unset, bool]):
        grant_transaction_id (Union[Unset, int]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        matter_note_id (Union[Unset, int]):
        only_unaccounted_for (Union[Unset, bool]):
        order (Union[Unset, ActivityindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        start_date (Union[Unset, str]):
        status (Union[Unset, ActivityindexStatus]):
        task_id (Union[Unset, int]):
        type_ (Union[Unset, ActivityindexType]):
        updated_since (Union[Unset, str]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActivityList, Error]
    """

    return sync_detailed(
        client=client,
        activity_description_id=activity_description_id,
        calendar_entry_id=calendar_entry_id,
        communication_id=communication_id,
        contact_note_id=contact_note_id,
        created_since=created_since,
        end_date=end_date,
        expense_category_id=expense_category_id,
        fields=fields,
        flat_rate=flat_rate,
        grant_transaction_id=grant_transaction_id,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        matter_note_id=matter_note_id,
        only_unaccounted_for=only_unaccounted_for,
        order=order,
        page_token=page_token,
        query=query,
        start_date=start_date,
        status=status,
        task_id=task_id,
        type_=type_,
        updated_since=updated_since,
        user_id=user_id,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    activity_description_id: Unset | int = UNSET,
    calendar_entry_id: Unset | int = UNSET,
    communication_id: Unset | int = UNSET,
    contact_note_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    end_date: Unset | str = UNSET,
    expense_category_id: Unset | int = UNSET,
    fields: Unset | str = UNSET,
    flat_rate: Unset | bool = UNSET,
    grant_transaction_id: Unset | int = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    matter_note_id: Unset | int = UNSET,
    only_unaccounted_for: Unset | bool = UNSET,
    order: Unset | ActivityindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    start_date: Unset | str = UNSET,
    status: Unset | ActivityindexStatus = UNSET,
    task_id: Unset | int = UNSET,
    type_: Unset | ActivityindexType = UNSET,
    updated_since: Unset | str = UNSET,
    user_id: Unset | int = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[ActivityList | Error]:
    """Return the data for all Activities

     Outlines the parameters, optional and required, used when requesting the data for all Activities

    Args:
        activity_description_id (Union[Unset, int]):
        calendar_entry_id (Union[Unset, int]):
        communication_id (Union[Unset, int]):
        contact_note_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        end_date (Union[Unset, str]):
        expense_category_id (Union[Unset, int]):
        fields (Union[Unset, str]):
        flat_rate (Union[Unset, bool]):
        grant_transaction_id (Union[Unset, int]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        matter_note_id (Union[Unset, int]):
        only_unaccounted_for (Union[Unset, bool]):
        order (Union[Unset, ActivityindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        start_date (Union[Unset, str]):
        status (Union[Unset, ActivityindexStatus]):
        task_id (Union[Unset, int]):
        type_ (Union[Unset, ActivityindexType]):
        updated_since (Union[Unset, str]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActivityList, Error]]
    """

    kwargs = _get_kwargs(
        activity_description_id=activity_description_id,
        calendar_entry_id=calendar_entry_id,
        communication_id=communication_id,
        contact_note_id=contact_note_id,
        created_since=created_since,
        end_date=end_date,
        expense_category_id=expense_category_id,
        fields=fields,
        flat_rate=flat_rate,
        grant_transaction_id=grant_transaction_id,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        matter_note_id=matter_note_id,
        only_unaccounted_for=only_unaccounted_for,
        order=order,
        page_token=page_token,
        query=query,
        start_date=start_date,
        status=status,
        task_id=task_id,
        type_=type_,
        updated_since=updated_since,
        user_id=user_id,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    activity_description_id: Unset | int = UNSET,
    calendar_entry_id: Unset | int = UNSET,
    communication_id: Unset | int = UNSET,
    contact_note_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    end_date: Unset | str = UNSET,
    expense_category_id: Unset | int = UNSET,
    fields: Unset | str = UNSET,
    flat_rate: Unset | bool = UNSET,
    grant_transaction_id: Unset | int = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    matter_note_id: Unset | int = UNSET,
    only_unaccounted_for: Unset | bool = UNSET,
    order: Unset | ActivityindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    start_date: Unset | str = UNSET,
    status: Unset | ActivityindexStatus = UNSET,
    task_id: Unset | int = UNSET,
    type_: Unset | ActivityindexType = UNSET,
    updated_since: Unset | str = UNSET,
    user_id: Unset | int = UNSET,
    x_api_version: Unset | str = UNSET,
) -> ActivityList | Error | None:
    """Return the data for all Activities

     Outlines the parameters, optional and required, used when requesting the data for all Activities

    Args:
        activity_description_id (Union[Unset, int]):
        calendar_entry_id (Union[Unset, int]):
        communication_id (Union[Unset, int]):
        contact_note_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        end_date (Union[Unset, str]):
        expense_category_id (Union[Unset, int]):
        fields (Union[Unset, str]):
        flat_rate (Union[Unset, bool]):
        grant_transaction_id (Union[Unset, int]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        matter_note_id (Union[Unset, int]):
        only_unaccounted_for (Union[Unset, bool]):
        order (Union[Unset, ActivityindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        start_date (Union[Unset, str]):
        status (Union[Unset, ActivityindexStatus]):
        task_id (Union[Unset, int]):
        type_ (Union[Unset, ActivityindexType]):
        updated_since (Union[Unset, str]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActivityList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            activity_description_id=activity_description_id,
            calendar_entry_id=calendar_entry_id,
            communication_id=communication_id,
            contact_note_id=contact_note_id,
            created_since=created_since,
            end_date=end_date,
            expense_category_id=expense_category_id,
            fields=fields,
            flat_rate=flat_rate,
            grant_transaction_id=grant_transaction_id,
            ids=ids,
            limit=limit,
            matter_id=matter_id,
            matter_note_id=matter_note_id,
            only_unaccounted_for=only_unaccounted_for,
            order=order,
            page_token=page_token,
            query=query,
            start_date=start_date,
            status=status,
            task_id=task_id,
            type_=type_,
            updated_since=updated_since,
            user_id=user_id,
            x_api_version=x_api_version,
        )
    ).parsed
