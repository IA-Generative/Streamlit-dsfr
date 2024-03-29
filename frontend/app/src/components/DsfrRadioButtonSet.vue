<script setup lang="ts">
import { ref } from 'vue'
import { Streamlit } from '~/stcomponentlib'
import { DsfrRadioButtonSet } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps'

useStreamlit()

interface Option
{
	label?: string
	value?: string
	disabled?: boolean
	hint?: string
}

const props = defineProps<
	ComponentProps<{
		// Props
		inline?: boolean
		modelValue?: string
		small?: boolean
		options?: Option[]
		titleId?: string
		disabled?: boolean
		required?: boolean
		name?: string
		errorMessage?: string
		validMessage?: string
		// Slots
		legend?: string
		requiredTip?: string
		default?: string
	}>
>()

const value = ref<string>(props.args.modelValue ?? '')

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
		{
			option.disabled = true
			return option
		},
	)
}

function onUpdateModelValue()
{
	Streamlit.setComponentValue(value.value)
}
</script>

<template>
	<div class="component">
		<DsfrRadioButtonSet
			v-bind="props.args"
			:options="parseOptions(props.args.options)"
			v-model="value"
			@update:modelValue="onUpdateModelValue"
		>
			<template #required-tip v-if="props.args.requiredTip">
				{{ props.args.requiredTip }}
			</template>
		</DsfrRadioButtonSet>
	</div>
</template>

<style scoped>
.component :deep(.fr-fieldset) {
	margin-bottom: -.5rem;
}
.component :deep(.fr-fieldset__legend) {
	padding-bottom: .5rem;
}
.component :deep(.fr-fieldset__element) {
	margin-bottom: .5rem;
}
</style>
