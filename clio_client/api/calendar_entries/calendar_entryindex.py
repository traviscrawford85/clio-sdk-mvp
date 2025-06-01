from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.calendar_entry_list import CalendarEntryList
from ...models.calendar_entryindex_source import CalendarEntryindexSource
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    calendar_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    expanded: Unset | bool = UNSET,
    external_property_name: Unset | str = UNSET,
    external_property_value: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    from_: Unset | str = UNSET,
    has_court_rule: Unset | bool = UNSET,
    ids: Unset | int = UNSET,
    is_all_day: Unset | bool = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    owner_entries_across_all_users: Unset | bool = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    source: Unset | CalendarEntryindexSource = UNSET,
    to: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    visible: Unset | bool = UNSET,
    x_api_version: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["calendar_id"] = calendar_id

    params["created_since"] = created_since

    params["expanded"] = expanded

    params["external_property_name"] = external_property_name

    params["external_property_value"] = external_property_value

    params["fields"] = fields

    params["from"] = from_

    params["has_court_rule"] = has_court_rule

    params["ids[]"] = ids

    params["is_all_day"] = is_all_day

    params["limit"] = limit

    params["matter_id"] = matter_id

    params["owner_entries_across_all_users"] = owner_entries_across_all_users

    params["page_token"] = page_token

    params["query"] = query

    json_source: Unset | str = UNSET
    if not isinstance(source, Unset):
        json_source = source.value

    params["source"] = json_source

    params["to"] = to

    params["updated_since"] = updated_since

    params["visible"] = visible

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/calendar_entries.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CalendarEntryList | Error | None:
    if response.status_code == 200:
        response_200 = CalendarEntryList.from_dict(response.json())

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
) -> Response[CalendarEntryList | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    calendar_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    expanded: Unset | bool = UNSET,
    external_property_name: Unset | str = UNSET,
    external_property_value: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    from_: Unset | str = UNSET,
    has_court_rule: Unset | bool = UNSET,
    ids: Unset | int = UNSET,
    is_all_day: Unset | bool = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    owner_entries_across_all_users: Unset | bool = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    source: Unset | CalendarEntryindexSource = UNSET,
    to: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    visible: Unset | bool = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[CalendarEntryList | Error]:
    """Return the data for all CalendarEntries

     Outlines the parameters, optional and required, used when requesting the data for all
    CalendarEntries

    Args:
        calendar_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        expanded (Union[Unset, bool]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        from_ (Union[Unset, str]):
        has_court_rule (Union[Unset, bool]):
        ids (Union[Unset, int]):
        is_all_day (Union[Unset, bool]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        owner_entries_across_all_users (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        source (Union[Unset, CalendarEntryindexSource]):
        to (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        visible (Union[Unset, bool]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CalendarEntryList, Error]]
    """

    kwargs = _get_kwargs(
        calendar_id=calendar_id,
        created_since=created_since,
        expanded=expanded,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        from_=from_,
        has_court_rule=has_court_rule,
        ids=ids,
        is_all_day=is_all_day,
        limit=limit,
        matter_id=matter_id,
        owner_entries_across_all_users=owner_entries_across_all_users,
        page_token=page_token,
        query=query,
        source=source,
        to=to,
        updated_since=updated_since,
        visible=visible,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    calendar_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    expanded: Unset | bool = UNSET,
    external_property_name: Unset | str = UNSET,
    external_property_value: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    from_: Unset | str = UNSET,
    has_court_rule: Unset | bool = UNSET,
    ids: Unset | int = UNSET,
    is_all_day: Unset | bool = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    owner_entries_across_all_users: Unset | bool = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    source: Unset | CalendarEntryindexSource = UNSET,
    to: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    visible: Unset | bool = UNSET,
    x_api_version: Unset | str = UNSET,
) -> CalendarEntryList | Error | None:
    """Return the data for all CalendarEntries

     Outlines the parameters, optional and required, used when requesting the data for all
    CalendarEntries

    Args:
        calendar_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        expanded (Union[Unset, bool]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        from_ (Union[Unset, str]):
        has_court_rule (Union[Unset, bool]):
        ids (Union[Unset, int]):
        is_all_day (Union[Unset, bool]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        owner_entries_across_all_users (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        source (Union[Unset, CalendarEntryindexSource]):
        to (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        visible (Union[Unset, bool]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CalendarEntryList, Error]
    """

    return sync_detailed(
        client=client,
        calendar_id=calendar_id,
        created_since=created_since,
        expanded=expanded,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        from_=from_,
        has_court_rule=has_court_rule,
        ids=ids,
        is_all_day=is_all_day,
        limit=limit,
        matter_id=matter_id,
        owner_entries_across_all_users=owner_entries_across_all_users,
        page_token=page_token,
        query=query,
        source=source,
        to=to,
        updated_since=updated_since,
        visible=visible,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    calendar_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    expanded: Unset | bool = UNSET,
    external_property_name: Unset | str = UNSET,
    external_property_value: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    from_: Unset | str = UNSET,
    has_court_rule: Unset | bool = UNSET,
    ids: Unset | int = UNSET,
    is_all_day: Unset | bool = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    owner_entries_across_all_users: Unset | bool = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    source: Unset | CalendarEntryindexSource = UNSET,
    to: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    visible: Unset | bool = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[CalendarEntryList | Error]:
    """Return the data for all CalendarEntries

     Outlines the parameters, optional and required, used when requesting the data for all
    CalendarEntries

    Args:
        calendar_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        expanded (Union[Unset, bool]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        from_ (Union[Unset, str]):
        has_court_rule (Union[Unset, bool]):
        ids (Union[Unset, int]):
        is_all_day (Union[Unset, bool]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        owner_entries_across_all_users (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        source (Union[Unset, CalendarEntryindexSource]):
        to (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        visible (Union[Unset, bool]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CalendarEntryList, Error]]
    """

    kwargs = _get_kwargs(
        calendar_id=calendar_id,
        created_since=created_since,
        expanded=expanded,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        from_=from_,
        has_court_rule=has_court_rule,
        ids=ids,
        is_all_day=is_all_day,
        limit=limit,
        matter_id=matter_id,
        owner_entries_across_all_users=owner_entries_across_all_users,
        page_token=page_token,
        query=query,
        source=source,
        to=to,
        updated_since=updated_since,
        visible=visible,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    calendar_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    expanded: Unset | bool = UNSET,
    external_property_name: Unset | str = UNSET,
    external_property_value: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    from_: Unset | str = UNSET,
    has_court_rule: Unset | bool = UNSET,
    ids: Unset | int = UNSET,
    is_all_day: Unset | bool = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    owner_entries_across_all_users: Unset | bool = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    source: Unset | CalendarEntryindexSource = UNSET,
    to: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    visible: Unset | bool = UNSET,
    x_api_version: Unset | str = UNSET,
) -> CalendarEntryList | Error | None:
    """Return the data for all CalendarEntries

     Outlines the parameters, optional and required, used when requesting the data for all
    CalendarEntries

    Args:
        calendar_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        expanded (Union[Unset, bool]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        from_ (Union[Unset, str]):
        has_court_rule (Union[Unset, bool]):
        ids (Union[Unset, int]):
        is_all_day (Union[Unset, bool]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        owner_entries_across_all_users (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        source (Union[Unset, CalendarEntryindexSource]):
        to (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        visible (Union[Unset, bool]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CalendarEntryList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            calendar_id=calendar_id,
            created_since=created_since,
            expanded=expanded,
            external_property_name=external_property_name,
            external_property_value=external_property_value,
            fields=fields,
            from_=from_,
            has_court_rule=has_court_rule,
            ids=ids,
            is_all_day=is_all_day,
            limit=limit,
            matter_id=matter_id,
            owner_entries_across_all_users=owner_entries_across_all_users,
            page_token=page_token,
            query=query,
            source=source,
            to=to,
            updated_since=updated_since,
            visible=visible,
            x_api_version=x_api_version,
        )
    ).parsed
