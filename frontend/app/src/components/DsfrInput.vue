<script setup lang="ts">
import { reactive, ref } from 'vue'
import { Streamlit } from '~/stcomponentlib'
import { DsfrInput } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		disabled?: boolean
		// Props
		labelVisible?: boolean
		hint?: string
		modelValue?: string
		id?: string
		descriptionId?: string
		isInvalid?: boolean
		isValid?: boolean
		isWithWarning?: boolean
		labelClass?: string
		wrapperClass?: string
		// Slots
		label?: string
		requiredTip?: string
	}>
>()

const lastValue = ref('')
const value = ref('')

// Bind the input value to `value`
// Update the Steamlit value when:
// - the input lose focus, if the value has changed
// - the user press enter, if the input is focused and the value has changed

const onInput = (event: Event) =>
	{
		const target = event.target as HTMLInputElement
		value.value = target.value
	}

const onBlur = () =>
	{
		if (value.value !== lastValue.value)
		{
			lastValue.value = value.value
			Streamlit.setComponentValue(value.value)
		}
	}

const onKeydown = (event: KeyboardEvent) =>
	{
		if (event.key === 'Enter' && value.value !== lastValue.value)
		{
			lastValue.value = value.value
			Streamlit.setComponentValue(value.value)
		}
	}
</script>

<template>
	<div class="component">
		<DsfrInput
			v-bind="props.args"
			:disabled="props.disabled || props.args.disabled"
			v-model="value"
			@input="onInput"
			@blur="onBlur"
			@keydown="onKeydown"
		>
			<template #label v-if="props.args.label">
				{{ props.args.label }}
			</template>
			<template #required-tip v-if="props.args.requiredTip">
				{{ props.args.requiredTip }}
			</template>
		</DsfrInput>
	</div>
</template>

<style scoped>
.component {
	margin: 4px; /* Margin for the input outline on focus */
}
</style>
