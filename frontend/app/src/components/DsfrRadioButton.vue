<script setup lang="ts">
import { reactive, ref } from 'vue'
import { Streamlit } from '~/stcomponentlib'
import { DsfrRadioButton } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps'

useStreamlit()

interface Option
{
	label?: string
	value?: string
	disabled?: boolean
	hint?: string
	name?: string
}

const props = defineProps<
	ComponentProps<{
		options?: Option[]
		disabled?: boolean
		// Props
		modelValue?: string
		small?: boolean
		id?: string
		name?: string
		inline?: boolean
		vakue?: string
		hint?: string
		img?: string
		// Slots
		label?: string
		requiredTip?: string
	}>
>()

function parseOptions(options: Option[] | undefined): Option[]
{
	if (!options)
	{
		return []
	}

	// Check for global disabled state
	if (!props.disabled && !props.args.disabled)
	{
		return options
	}

	// Global disabled state is true
	return options.map(option =>
		({
			label: option.label,
			value: option.value,
			disabled: true, // Overriden
			hint: option.hint,
			name: option.name,
		}),
	)
}

function onUpdateModelValue(event: Event)
{
	const target = event.target as HTMLInputElement
	Streamlit.setComponentValue(target.value)
}
</script>

<template>
	<div class="component">
		<DsfrRadioButton
			v-bind="props.args"
			:options="parseOptions(props.args.options)"
			@update:modelValue="onUpdateModelValue"
		>
			<template #label v-if="props.args.label">
				{{ props.args.label }}
			</template>
			<template #required-tip v-if="props.args.requiredTip">
				{{ props.args.requiredTip }}
			</template>
		</DsfrRadioButton>
	</div>
</template>

<style scoped>
.component {
	margin: 4px; /* Margin for the input outline on focus */
}
</style>
