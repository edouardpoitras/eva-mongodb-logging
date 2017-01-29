MongoDB Logging
===============

A plugin that stores all Eva log messages to MongoDB.

This plugin will only be able to start logging after it has been enabled during the boot process.
It may not reveal issues with parsing the plugins directories, the config files, and may not catch any plugin errors that occur before this plugin's instantiation.

## Installation

Can be easily installed through the Web UI by using [Web UI Plugins](https://github.com/edouardpoitras/eva-web-ui-plugins).

Alternatively, add `mongodb_logging` to your `eva.conf` file in the `enabled_plugins` option list and restart Eva.

## Usage

Nothing to be done on the user's part.

See the [Web UI Logs](https://github.com/edouardpoitras/eva-web-ui-logs) plugin in order to browse all log messages in the Web UI.

## Configuration

Default configurations can be changed by adding a `mongodb_logging.conf` file in your plugin configuration path (can be configured in `eva.conf`, but usually `~/eva/configs`).

To get an idea of what configuration options are available, you can take a look at the `mongodb_logging.conf.spec` file in this repository, or use the [Web UI Plugins](https://github.com/edouardpoitras/eva-web-ui-plugins) plugin and view them at `/plugins/configuration/mongodb_logging`.

Here is a breakdown of the available options:

    log_mongo_collection
        Type: String
        Default: 'logs'
        The MongoDB collection to store all log messages.
